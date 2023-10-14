# TODO Найдите количество книг, которое можно разместить на дискете
disket=1.44*1024*1024
x=100
y=50
z=25
size=4
x_size=y*z*size
book_size=x_size*x
book_disket=disket//book_size
print("Количество книг, помещающихся на дискету:", int(book_disket))
