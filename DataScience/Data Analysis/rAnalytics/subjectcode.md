### Species별 Sepal.Length로 구분

```R
iris_data = iris
# 원본 데이터에 영향이 없도록 복사
library(dplyr)
# sorting을 위해 dplyr 패키지 사용
iris_data = iris %>%
    group_by(Species) %>%
    summarise(Sepal.Length = Sepal.Length(mean))
# 종별로 구분하여 평균값을 구함

ggplot(iris_data, aes(x = Species, y = Sepal.Length, fill = Sepal.Length)) +
# fill = 그래프에 표시될 자료
    geom_bar(stat = 'identity') +
    # 막대의 높이를 데이터의 실제 값으로 지정
    scale_fill_gradient(low = 'darkblue', higih = 'blue') +
    # 값에 맞게 그라디에이션을 적용
    theme_minimal()
```

```R
diamonds_data = diamonds %>% subset(diamonds, select = c('clarity', 'price', 'cut', 'color'))
# 필요한 컬럼만 subset

diamonds_data = diamonds_data %>%
    filter(cut == 'Ideal', color == 'E')
# 원하는 조건의 데이터만 filter

price_avg = diamonds_data %>%
    group_by(clarity) %>%
    summarise_all(mean)
# 투명도 별로 구분하여 평균값 도출

diamonds_data = subset(diamonds_data, select = c('clarity', 'price'))
# 필요 없는 컬럼 제거

ggplot(price_avg, aes(x = clarity,
                     y = price,
                     fill = price)) + 
    geom_bar(stat = 'identity') + 
    scale_fill_gradient(low = 'darkblue', high = 'lightblue') + 
    theme_minimal()
```
- 깔끔한 버전
```R
library(dplyr)
library(ggplot2)

diamonds_data = diamonds %>%
    filter(cut == 'Ideal', color == 'E') %>%
    # 대부분의 경우 subset보다 filter함수를 사용하는 것이 권장됨
    select(clarity, price)
    # cut과 color로 필터링한뒤 필요한 컬럼만 가져온다

price_avg = diamonds_data %>%
    group_by(clarity) %>%
    summarise(price = mean(price))

ggplot(price_avg, aes(x = clarity, y = price, fill = price)) +
    geom_bar(stat = 'identity') +
    scale_fill_gradient(low = 'darkblue', high = 'lightblue') +
    theme_minimal()
```
```R
iris_data2 = iris %>%
    group_by(Species) %>%
    select(Sepal.Length, Sepal.Width)
# 필요한 데이터 추출

scatter_plot = ggplot(iris_data2, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
# color : 지정컬럼의 값 별로 색깔 구분
    geom_point(size = 3) + 
    # 굵기 3의 점 그래프
    theme(legend.position = 'none')
    # 범례 제거
    labs(x = 'Sepal.Length', y = 'Sepal.Width')
```

```R
# PLOT1
gg = ggplot(data = iris,
            aes(x = Sepal.Length,
                y = Sepal.Width,
                color = Species)) + 
  geom_point(size = 3) + 
  theme(legend.position = "none")

scatter_plot = ggMarginal(p = gg,
           groupColour = TRUE,
           groupFill = TRUE)

# PLOT2
iris_plot2_data = iris %>%
    filter(Species == 'setosa')

plot2 = ggplot(data = iris_plot2_data,
            aes(x = Sepal.Length,
                y = Sepal.Width)) + 
    geom_point(size = 3) + 
    theme(legend.position = "none")

# PLOT3
iris_plot3_data = iris %>%
    filter(Species == 'versicolor')

plot2 = ggplot(data = iris_plot3_data,
            aes(x = Sepal.Length,
                y = Sepal.Width)) + 
    geom_point(size = 3) + 
    theme(legend.position = "none")

# PLOT4

```

```R
# 막대 그래프
cut_count = diamonds %>%
    group_by(cut) %>%
    summarise(count = n())

ggplot(cut_count, aes(x = cut, y = count, fill = cut)) +
+     geom_bar(stat = "identity", width = 1) +
+     labs(x = NULL, y = NULL) +
+     scale_fill_manual(values = c("#800080", "#000080", "#008B8B", "#00FF00", "yellow"))+
+     coord_flip() + 
+     theme(legend.position = 'none')

# 파이차트
cut_count2 <- cut_count %>%
    mutate(percent = count / sum(count) * 100) %>%
    arrange(desc(cut))

ggplot(cut_count2, aes(x = count, y = cut, fill = cut)) 
# x, y값을 도치
    geom_bar(stat = "identity", width = 1) +
    labs(x = NULL, y = NULL) +
    scale_fill_manual(values = c("#800080", "#000080", "#008B8B", "#00FF00", "yellow"))+
    coord_polar(theta = "y") + 
    theme(legend.position = 'none')
```

```R
heatmap_data <- diamonds %>%
    group_by(cut, color) %>%
    summarise(price_mean = mean(price))

ggplot(heatmap_data, aes(x = color, y = cut)) +
    geom_tile(aes(fill = price_mean), width = 1, height = 1) +
    scale_fill_gradient(low = '#0000FF', high ='#FF0000') +
    labs(x = "color", y = "cut") +
    theme_minimal()
```

```R
boxplot = ggplot(diamonds, aes(x = color, y = carat, fill = color)) +
    geom_boxplot() +
    labs(x = "Color", y = "Carat") +
    theme_bw() +
    facet_wrap(~cut, ncol = 5)

boxplot = boxplot + 
    theme(legend.position = 'none')
```