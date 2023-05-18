from ...models import * #база данных

class DefinitionProduct():
    def __init__(self, user):
        self.user = user

    def getSelectedList(self):
        return SelectedProducts.objects.filter(user = self.user)
    
    def containst(self, list, product):
        temp = False
        if list.exist() == True: 
            for elem in list:
                if elem.product == product:
                    temp = True
        return temp
    
    def appendToSelectedList(self, productId):
        if productId != 'none': 
            if SelectedProducts.objects.filter(product = Flower.objects.get(pk=productId)).exists() == False:
                product = Flower.objects.get(pk=productId)
                if product.count >= 1:
                    SelectedProducts.objects.create(product=product, count=1, user=self.user)

    def deleteFromSelectedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if SelectedProducts.objects.filter(product = product).exists():
                SelectedProducts.objects.filter(product=product).delete()
    
    def getPurchasedList(self):
        return PurchasedProducts.objects.filter(user = self.user)
    
    def appendToPurchasedList(self, productId):
        if productId != 'none': 
            if PurchasedProducts.objects.filter(product = Flower.objects.get(pk=productId)).exists() == False:
                product = Flower.objects.get(pk=productId)
                if product.count >= 1:
                    PurchasedProducts.objects.create(product=product, count=1, user=self.user)

    def deleteFromPurchasedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if self.containst(PurchasedProducts.objects.filter(user=self.user), product):
                PurchasedProducts.objects.filter(product=product).delete()
    
    def getLikedList(self):
        return LikedProducts.objects.filter(user = self.user)
    
    def appendTokedList(self, productId):
        if productId != 'none':                
            product = Flower.objects.get(pk=productId)
            if self.containst(LikedProducts.objects.filter(user=self.user), product) == False:
                LikedProducts.objects.create(product=product, user=self.user)

    def deleteFromkedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if self.containst(LikedProducts.objects.filter(user=self.user), product):
                LikedProducts.objects.filter(product=product).delete()
