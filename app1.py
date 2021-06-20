a=[2,3,1]
b=[3,6,-2,-5,7,3]

def adjacentElementsProduct(a):
    l=len(a)
    product=[0]*(l-1)
    for i in range(0,l-1):
        product[i]=a[i]*a[i+1]
    result=max(product)
    pos=product.index(result)
    return result
print(6 == adjacentElementsProduct(a))
print(21 == adjacentElementsProduct(b))
