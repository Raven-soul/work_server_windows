#
#  definitionProduct.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 15.05.2023.
#

from ...models import * #база данных

class DefinitionProduct():
    def __init__(self, user):
        self.user = user
    
    def containst(self, isEmpty, list, product):
        temp = False
        if isEmpty == True: 
            for elem in list:
                if elem.product == product:
                    temp = True
        return temp
    
    #--------------------------------- SelectedList ------------------------------------------------ 

    def getSelectedList(self):
        return SelectedProducts.objects.filter(user = self.user)
    
    def appendToSelectedList(self, productId):
        if productId != 'none':                
            product = Flower.objects.get(pk=productId)
            if product.count >= 1:
                if self.containst(SelectedProducts.objects.filter(user=self.user).exists(), SelectedProducts.objects.filter(user=self.user), product) == False:
                    SelectedProducts.objects.create(product=product, count=1, user=self.user)

    def deleteFromSelectedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if self.containst(SelectedProducts.objects.filter(user=self.user).exists(), SelectedProducts.objects.filter(user=self.user), product):
                SelectedProducts.objects.get(product=product, user= self.user).delete()
    
    #--------------------------------- PurchasedList ------------------------------------------------ 

    def getPurchasedList(self):
        return PurchasedProducts.objects.filter(user = self.user)
    
    def appendToPurchasedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if product.count >= 1:
                PurchasedProducts.objects.create(product=product, count=1, user=self.user)

    def deleteFromPurchasedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if self.containst(PurchasedProducts.objects.filter(user=self.user).exists(), PurchasedProducts.objects.filter(user=self.user), product):
                costProduct = PurchasedProducts.objects.get(product=product, user= self.user)
                product.count = product.count + costProduct.count
                product.save(update_fields=["count"])
                costProduct.delete()
    
    #--------------------------------- LikedList ------------------------------------------------ 

    def getLikedList(self):
        return LikedProducts.objects.filter(user = self.user)
    
    def appendToLikedList(self, productId):
        if productId != 'none':                
            product = Flower.objects.get(pk=productId)
            if self.containst(LikedProducts.objects.filter(user=self.user).exists(), LikedProducts.objects.filter(user=self.user), product) == False:
                LikedProducts.objects.create(product=product, user=self.user)

    def deleteFromLikedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if self.containst(LikedProducts.objects.filter(user=self.user).exists(), LikedProducts.objects.filter(user=self.user), product):
                LikedProducts.objects.get(product=product, user= self.user).delete()
