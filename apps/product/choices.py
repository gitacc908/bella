PINK = 0
WHITE = 1
LIGHT_BLUE = 2
CYAN = 3
LIGHT_GREEN = 4
BROWN = 5
GREY = 6

COLOR_CHOICES = (
    (PINK, 'Розовый'),
    (WHITE, 'Белый'),
    (LIGHT_BLUE, 'Светло-синий'),
    (CYAN, 'Голубой'),
    (LIGHT_GREEN, 'Светло-Зеленый'),
    (BROWN, 'Коричневый'),
    (GREY, 'Серый'),
)


ATLAS = 7
BATIST = 8
BENGALIN = 9
BUCKLE = 10
OGG = 11
POLYESTER = 12

CLOTHING_FABRIC_CHOICES = (
    (ATLAS, 'Атлас'),
    (BATIST, 'Батист'),
    (BENGALIN, 'Бенгалин'),
    (BUCKLE, 'Букле'),
    (OGG, 'Бязь'),
    (POLYESTER, 'Полиэстер'),
)


XS = 42
S = 44
M = 46
L = 48
XL = 50
XXL = 52
XXXL = 54
BXL = 56
BXXL = 58
BXXXL = 60

SIZE_RANGE_CHOICES = (
    (XS, '42'),
    (S, '44'),
    (M, '46'),
    (L, '48'),
    (XL, '50'),
    (XXL, '52'),
    (XXXL, '54'),
    (BXL, '56'),
    (BXXL, '58'),
    (BXXXL, '60'),
)

LENGTH_RANGE_CHOICES = (
    (XS, '82-85'),
    (S, '86-89'),
    (M, '90-93'),
    (L, '94-97'),
    (XL, '98-102'),
    (XXL, '103-107'),
    (XXXL, '108-113'),
    (BXL, '114-119'),
)


A_SILHOUETTE = 13
HIGH_WAIST = 14
AMPIR = 15
GREEK_STYLE = 16
RETRO_STYLE = 17
VINTAGE_STYLE = 18

FASHION_CHOICES = (
    (A_SILHOUETTE, 'А-Силуэт'),
    (HIGH_WAIST, 'Завышенная талия'),
    (AMPIR, 'Ампир'),
    (GREEK_STYLE, 'Греческий стиль'),
    (RETRO_STYLE, 'Ретро стиль'),
    (VINTAGE_STYLE, 'Винтаж стиль'),
)
