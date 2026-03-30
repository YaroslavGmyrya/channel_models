# Теория случайных процессов в DSP

## Основы теории вероятности

**Случайной величиной** называется функция ξ, заданная на пространстве элементарных исходов Ω = {ω} случайных испытаний и ставящая в соответствие каждому элементарному исходу ω ∈ Ω число ξ = ξ(ω).

Менее строгое определение:

**Случайная величина** - правило, по которому случайный исход превращается в число.

[![image.png](https://i.postimg.cc/5y61Yq9c/image.png)](https://postimg.cc/WqLxxZJS)

СВ имеют:
 * **Закон распределения** (ряд или плотность распределения) 
 * **Функцию распределения** 
 
А также **числовые характеристики:** 
* Математическое ожидание
* Дисперсия и среднеквадратичное отклонение

**Законом распределения СВ** - соотношение, устанавливающее связь между возможными значениями и соответствующими им вероятностями.

Часто задается в виде таблицы:

[![image.png](https://i.postimg.cc/kGc1mkP6/image.png)](https://postimg.cc/V0JB9Z6m)

Функцией распределения случайной величины ξ называется функция $F_ξ (x)$, выражающая для каждого значения x вероятность того, что случайная величина ξ примет значение, меньшее x.

![](data:image/png;base64,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)

Если посмотреть на таблицу выше, то:

F(0) = P{$\xi$ < 0} = 0
F(1) = P{$\xi$ < 1} = 0 + 0.25 = 0.25
F(2) = P{$\xi$ < 2} = 0 + 0.25 + 0.5 = 0.75
F(3) = P{$\xi$ < 3} = 0 + 0.25 + 0.5 + 0.25 = 1.0

Свойства функции распределения:
* $0 \le F(x) \le 1,  -\inf < x < \inf$ (значения заключены между нулем и единицей)
* Если $x_1 < x_2$, то $F(x_1) \le F(x_2)$ (функция возрастающая)
* Непрерывна слева
* $\lim_{x->-\inf}F(x) = 0, \lim_{x->\inf}F(x) = 1$ (слева только нулевые значения, а справа ненулевые, поэтому функция стремится к 1)

**Случайные величины бывают:**
* Дискретные - могут принимать счетное количество различных значений.
* Непрерывные - могут принимать бесконечное количество различных значений.

### Дискретные СВ
**СВ называется дискретной**, если множество ее возможных значений представляет собой конечную или бесконечную последовательность чисел x1 , x2 , … , xn , … .

Способы описания ДСВ:

**Закон распределения** дискретной случайной величины обычно задается рядом распределения.

[![image.png](https://i.postimg.cc/kGc1mkP6/image.png)](https://postimg.cc/V0JB9Z6m)

**Многоугольник распределения** дискретной случайной величины – ломаная на плоскости, соединяющая последовательно точки с координатами $( x_k, p_k )$, k = 1, 2, …, n

[![image.png](https://i.postimg.cc/W3DJXqsV/image.png)](https://postimg.cc/0MsQNQ6X)

**Функция распределения** является разрывной, ступенчатой функцией со скачками в точках, координаты равны значениям случайной величины, а величины скачков равны соответствующим им вероятностям.

[![image.png](https://i.postimg.cc/KcB1j2zQ/image.png)](https://postimg.cc/jCqx3ByJ)

Числовые характеристики СВ:

**Математическим ожиданием (средним значением)** дискретной случайной величины называется величина Mξ, равная сумме произведений значений xk случайной величины ξ на соответствующие им вероятности pk:

$$\boxed{M(\xi)=\sum_{k=1}^{\inf}x_kp_k}$$

[![image.png](https://i.postimg.cc/J0Qs6NH1/image.png)](https://postimg.cc/ctr168cj)

[![image.png](https://i.postimg.cc/FRM6Wc5n/image.png)](https://postimg.cc/VrF45JNj)

# Модели каналов

## AWGN

**AWGN** - модель канала, в которой учитывается только тепловой шум. Не учитываются замирания, интерференция и прочие процессы.

**A - additional** - означает, что шум добавочный, т.е суммируется с сигналом, а не перемножается.
**A - white**  - означает, что процесс содержит на всех частотах одинаковую мощность. Это аналогично белому свету, который содержит на всех длинах волн видимого спектра одинаковое кол-во энергии.
**A - gaussian** - амплитуда распределена по Гауссу (нормально)
**N - noise** - просто означает, что это не полезный сигнал.

Сигнал на приеме можно записать как:

$$y = x+n$$
где n - белый шум.

### Проверка свойств нормального распределения

У нормального распределения должна быть нулевая автокорреляция (кроме лага равного 0), а также спектральная плотность распределения должна быть константой.

[![image.png](https://i.postimg.cc/hPnS8jZR/image.png)](https://postimg.cc/py0bR2ts)

На графиках выше изображены:

1. СВ с нормальным распределением
2. Спектральная плотность распределения. Она не равна константе, т.к экспериментальные данные.
3. Автокорреляционная функция. Есть один явный пик при нулевом лаге. При остальных лагах значение колеблится около нуля.
4. Плотность распределения. Имеет вид колокола, что говорит о том, что это действительно нормальное распределение.

### Принцип работы модели

1. На вход модели подается сигнал (комплексные отсчеты) и уровень **SNR** на приеме.
2. Модель находит среднюю мощность сигнала как $\frac{1}{N}\sum_{n=1}^{N}s[n]^2$, где N - длина сигнала (кол-во семплов).
3. Находит мощность шума (дисперсию) как $P_n = \frac{P_{signal}}{Rx_{SNR}}$.
4. Зная дисперсию, модель генерирует белый шум и добавляет к сигналу.

### Методы борьбы с AWGN:

В канале AWGN оптимальный детектор — **детектор максимального правдоподобия (ML)**

Он выбирает символ, который ближе всего к принятому сигналу (какой точке на созвездии символ ближе).

Для BPSK сигнала детектор очень простой: если реальная часть больше 0, то это 1, а иначе - ноль.

### Метод оценки канала

Самой простой оценкой канала является **BER (Bit Error Rate)** - битовая ошибка, которая равна $\frac{Кол-во \ совпавших \ бит}{Общее \ кол-во \ бит}$.

Для ее расчета по сути просто необходимо сравнить поэлементно 2 массива битов: который передавали и который приняли.

##### Теоретический BER

Для определения теоретического BER используется **Q-функция** - хвост нормального распределения. Показывает вероятность того, что СВ больше какого-то значения.

$$Q(x)=\frac{1}{\sqrt{2π}}​​∫_0^x​e^{\frac{−t^2}{2}}dt$$

$$BER_{theory} = Q(\sqrt{SNR})$$

### Проверка модели

Подадим на модель разные фиксированный сигнал и разные SNR (от 0 до 30). Рассчитаем теоретический и экспериментальный BER:

[![image.png](https://i.postimg.cc/sxmNbSbz/image.png)](https://postimg.cc/T5y0DyRN)

Теория с экспериментом точно не совпадает, но имеет одинаковое поведение (убывает экспоненциально). Из этого можно сделать вывод, что модель построена верно.


## Rayleigh channel

### Распределение Релея

**Распределение Релея** — это непрерывное распределение вероятностей, которое возникает как распределение **модуля двумерной гауссовской случайной величины**.

Пусть есть две независимые друг от друга случайной величины $N_1(\mu, \sigma^2)$ и $N_2(\mu, \sigma^2)$, которые распределены нормально.

Представим $N_1 и N_2$ в виде одного комплексного числа, где реальная часть будет равна $N_1$, а мнимая - $N_2$. Такое распределение называется **комплексной гауссовской случайной величиной** и записывается как $C = (N_1(\mu, \sigma^2), N_2(\mu, \sigma^2))$.

**Распределением Релея** называется |C|, т.е 

$$R = \sqrt{N_1(\mu, \sigma^2)^2+ N_2(\mu, \sigma^2)^2}$$

$N_1$ и $N_2$ показывают распределение точек по координатам X и Y, а распределение Релея общее отклонение от нуля.

#### Плотность и функция распределения
[![image.png](https://i.postimg.cc/j5ZJyG3j/image.png)](https://postimg.cc/7GJ6kQkv)

##### PDF
Теоретическая плотность распределения:

$$PDF = \frac{r}{\sigma^2}e^{\frac{-r^2}{2\sigma^2}}$$

Для построения эмпирической CDF/PDF используется функция hist  модуля pyplot.

##### CDF

Теоретическая функция распределения:
 $$CDF = 1 - e^{\frac{-r^2}{2\sigma^2}}$$

### Применение в DSP

В цифровых системах мы работаем с комплексными отсчетами сигналов. Если на приемник приходит много отражений и каждое отражение рассматривать как случайную величину, то I и Q компоненты сигнала будут иметь распределение близкое к нормальному. Т.е результирующие отсчеты по сути будут **комплексной гауссовской случайной величиной**, а модуль сигнала - Релеевским распределением.

Модель Рэлея используется для моделирования замирания сигнала во времени, когда отсутствует прямой путь, но имеется множество его отражений, которые приходят на приемник и суммируются на антенне.

![](https://pysdr.org/_images/multipath.svg)

Переотраженные лучи имеют разные амплитуды, частоты (доплер), фазы. Из-за разницы в фазе может возникать следующая ситуация:

![](https://pysdr.org/_images/destructive_interference.svg)

Два отражения пришли в противофазе и в сумме дали 0. Может быть и обратная ситуация: сигналы могут прийти с "хорошей фазой"(кратной 2$\pi$) и тогда сигнал будет очень мощным.

![](https://pysdr.org/_images/multipath2.svg)


Модель Релея не дает прямого ответа на вопрос, как фактически смоделировать канал с ее помощью. Для генерации замирания Рэлея в симуляции необходимо использовать один из многих методов, например, метод Кларка или Джейкса.

Модель Джейкса предлагает симулировать многолучевость путем сложения синусоид (SOS, sum-of-sinusoids), а не рассчитыванием поведения каждого отдельного луча, что очень трудно вычислительно и математически.

Складывая большое число синусоид, удается добиться правильных статистических свойств канала.

В методе используются синусоиды с определенными частотами, которые называются доплеровскими.

**Частота Доплера** — это величина сдвига частоты сигнала из-за относительного движения между передатчиком, приёмником или отражателем.

Вычисляется как:

$$f = f_D*cos\alpha$$

Здесь $f_D$ - максимальная частота доплеровского сдвига, $\alpha$ - угол приема сигнала (под каким углом сигнал приходит на приемник).

Максимальная частота доплеровского сдвига:

$$f_D = \frac{v*f_c}{c}$$

Здесь $v$ - скорость движения приемника/передатчика, $f_c$ - несущая частота, c - скорость света ($3*10^8$).

Углы $\alpha$ можно вычислять разными способами, но самый простой - взять точки на окружности от 0 до 2$\pi$ с равномерным шагом, т.е, если мы суммируем Nсинусоид, то получим следующие углы:

$$\alpha = \frac{2\pi}{N}k$$

где k = 0,1,2,3...N

Зная всё, что указано выше, можно перейти к суммированию синусоид и построению коэффициента канала:

$$h = \sum_{n=0}^Ne^{i(2\pi *f_i*t+\phi_n)}$$

Здесь $f_i$ - текущий доплеровский сдвиг, $\phi_n$ - случайная фаза луча (случайное число от 0 до 2$\pi$)

$$f_i = f_D*cos(\alpha[i])$$

Алгоритм работы модели:
1. Задать начальные параметры ($f_c, v, N)$
2. Высчитать $f_D, \alpha$
3. Суммирование синусоид с вычислением для каждой синусоиды ($f_i и \phi_i)$

Полученная сумма должна иметь распределение Релея, т.к $e^{i(2\pi *f_i*t+\phi_n)}$ можно представить как $cos(2\pi *f_i*t+\phi_n) + isin(2\pi *f_i*t+\phi_n)$. Суммируя такие синусоиды в достаточном количестве, по ЦПТ получим СП с нормальным распределением в мнимой и реальной части, а модуль такого СП будет имеет распределение Релея.

Построим теоретическую плотность распределения Релея и плотность, полученную экспериментальным путем

[![image.png](https://i.postimg.cc/Z54dpBnW/image.png)](https://postimg.cc/GHgt1pkR)

Экспериментальная плотность распределения близка к теоретической, значит, модель построена правильно.

Автокорреляция коэффициента канала должна в теории иметь вид функции Бесселя нулевого порядка. Экспериментальная автокорреляция отличается, но у обеих функций имеется общий характер поведения в области нуля.

Применим полученный коэффициент канала к сигналу и проанализируем его:

[![image.png](https://i.postimg.cc/8cRGGW5J/image.png)](https://postimg.cc/SYx37nck)

После прохождения через канал сигнал становится зашумленным, но все еще остается похожим на прямоугольный.

Огибающая сигнала имеет распределение Релея, что говорит о том, что модель канала верная.

Автокорреляция сигнала также схожа с функцией Бесселя нулевого порядка.

Зная плотность распределения сигнала, мы можем вычислить вероятность того, что значение принятого сигнала окажется в определенном диапазоне, проинтегрировав плотность распределения сигнала на заданном диапазоне.

Вычислив функцию распредления сигнала, мы можем найти вероятность того, что значения сигнала не превысит какое-то значение X. Например, по последнему графику видно, что сигнал не превысит значение -1 с вероятностью 0.2.

## Распределение Райса

Распределение Райса используется в моделях каналах, где есть один LOS луч, который явно выделяется по уровню энергии (т.к он не отражается и не теряет из-за этого энегрию).

![](https://pysdr.org/_images/multipath2.svg)

Плотность распределения Райса:

$$f_{rice}(x) = \frac{x}{\sigma^2}e^{-\frac{x^2+A^2}{2\sigma^2}}I_0(\frac{xA}{\sigma^2})$$

здесь $\sigma^2$ - дисперсия, A - амплитуда LOS луча, $I_0$ - модифицированная функция Бесселя 

$$A = \frac{P_{LOS}}{P_{scatter}}$$
где $P_{LOS}$ - мощность прямого луча, $P_{scatter}$ - мощность рассеянных лучей.

[![image.png](https://i.postimg.cc/CxD5cvb1/image.png)](https://postimg.cc/87pT5mKQ)

Если сравнивать плотность распределения Райса и Релея, то можно заметить, что в зависимости от параметра А пик сдвигается вправо, т.е, добавляя LOS компоненту, вероятность того, что сигнал примет значение около нуля становится меньше. Это логично, ведь имеется прямой луч с повышенной энергией, который прибавляется к сигналу и увеличивает значения сигнала.

## Модель канала Райса


Модель канала очень схожа с моделью Релея, но к сумме лучей добавляется прямой луч

$$h_{rice} = h_{rayleigh} + Ae^{e^{i\phi}}$$

Здесь $Ae^{e^{i\phi}}$ - прямой луч

Результаты:

При малых A разница между прошлой моделью и текущей не заметна

[![image.png](https://i.postimg.cc/52s34qsP/image.png)](https://postimg.cc/G4sYzYwY)

Увеличим параметр А в 10 раз

[![image.png](https://i.postimg.cc/h407R4yZ/image.png)](https://postimg.cc/fkJbxshY)

Сигнал на приеме стал более четким за счет того, что энергия прямого луча стала больше.

Плотность распределения сместилась от нуля в правую сторону, т.к вклад прямого луча стал очень большим.


На графике CDF появилось плато, которое говорит о том, что все значения от -1 до 1 (почти) равновероятны.

Таким образом можно сказать, что в канале очень важно наличие прямого луча от передатчика, т.к это очень влияет на качество принятого сигнала.
