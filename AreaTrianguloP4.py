#Fernando Donis 20210415
import cProfile
def main():
    class triangulo:
        pass
    p = triangulo()
    p.base = int(input("Ingrese su base:"))
    p.altura = int(input("Ingrese su altura:"))
    area = p.base*p.altura
    area/2

    print(area)


cProfile.run('main()')
