from django.shortcuts import render,redirect,get_object_or_404
from .models import Board
from .forms import BoardForm,BoardDetailForm

# Create your views here.
def b_list(request):

    # 로그인된 인증된 사람 인지 확인 합니다.
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        return render(request,'bbs/list.html',{'posts':posts})
    else:
        return redirect('home')

def b_create(request):
    if request.method == 'GET':
        board_form = BoardForm()
    else:
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            return redirect("bbs:b_list")

    return render(request,'bbs/create.html',{
        'board_form':board_form
    })

def b_detail(request,board_id):
    post = get_object_or_404(Board,id=board_id)

    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()
    # 입력양식이 모두 readonly로 변경

    return render(request,'bbs/detail.html',{
        'board_detail_form':board_detail_form
    })

def b_update(request,board_id):
    post = get_object_or_404(Board,id=board_id)     #post하나 가져오고
    board_detail_form = BoardDetailForm(instance=post)  #가져온 post로 값이 있는 폼만들기
    
    board_detail_form.show_board_update()  # 글제목, 작성자, 내용만 수정처리 됨

    return render(request,'bbs/update.html',{
        'board_detail_form':board_detail_form
    })


def b_update_process(request,board_id):
    # 수정처리 전(DB가 반영되기 전) POST
    post = get_object_or_404(Board,id=board_id)

    if request.method == "POST":
        #수정된 내용을 가지고 있는 ModelForm객체를 생성한거에요
        board_detail_form = BoardDetailForm(request.POST, instance=post)

        if board_detail_form.is_valid():
            board_detail_form.save()

            board_detail_form.show_board_detail() # 모두 readonly 변경

            return render(request,'bbs/detail.html',{'board_detail_form':board_detail_form})

    return redirect('home')

def b_delete(request,board_id):
    # 삭제할 post 1개 받아오고,  삭제하고,  리턴
    post = get_object_or_404(Board,id=board_id)
    post.delete()
    return redirect('bbs:b_list')

def b_like(request,board_id):
    post = get_object_or_404(Board,id=board_id)
    post.b_like_count += 1
    post.save()
    
    # 트랜젝션 처리를 하고 싶다면, 모델이 아닌 모델폼 객체를 사용해야 함
    # board_detail_form = BoardDetailForm(instance=post)
    # board_detail_form.b_like_count +=1
    # new_post =board_detail_form.save(commit=False)
    # board_detail_form.b_like_count =100
    # new_post.save()  #commit 처리 됨

    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()  #readonly

    return render(request,'bbs/detail.html', {
        'board_detail_form':board_detail_form
        })


def c_create(request,board_id):
    pass