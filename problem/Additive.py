"""sleep"""
import math as m
def main():
    """finish"""
    tri_a = (m.sin(m.radians(90)))+(m.sin(m.radians(60))**2)
    trib = (m.cos(m.radians((245**2))))+m.cos(m.radians(45+135))
    print(tri_a/trib)
    faca = m.factorial(16)*m.factorial(4)
    facb = m.factorial(8)
    print(faca/facb)
    srta = 15+25
    srtb = m.sqrt(((25-12)**2)+((12-15)**2))
    print(srta/srtb)
    logx = m.log10((1234**4))
    print(logx)
    logb = m.log(4234, 5)+m.log2(8191)+(m.log10(156154)*71)
    logc = m.log(777, 7)-m.log(888, 8)-m.log(999, 9)
    print(logb/logc)
main()
