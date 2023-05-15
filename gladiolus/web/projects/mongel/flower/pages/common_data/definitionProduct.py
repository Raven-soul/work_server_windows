from ...models import * #база данных

class DefinitionProduct():
    def __init__(self, user):
        self.user = user
        self.selectedList = SelectedProducts.objects.filter(user = user)
        self.purchasedList = PurchasedProducts.objects.filter(user = user)
        self.likedList = LikedProducts.objects.filter(user = user)

    def getSelectedList(self):
        return self.selectedList
    
    def appendToSelectedList(self, productId):
        if productId != 'none': 
            if SelectedProducts.objects.filter(product = Flower.objects.get(pk=productId)).exists() == False:
                product = Flower.objects.get(pk=productId)
                if product.count >= 1:
                    SelectedProducts.objects.create(product=product, count=1, user=self.user)
            else:
                print('product already exist')

    def deleteFromSelectedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if SelectedProducts.objects.filter(product = product).exists():
                SelectedProducts.objects.filter(product=product).delete()
    
    def getPurchasedList(self):
        return self.purchasedList
    
    def appendToPurchasedList(self, productId):
        if productId != 'none': 
            if PurchasedProducts.objects.filter(product = Flower.objects.get(pk=productId)).exists() == False:
                product = Flower.objects.get(pk=productId)
                if product.count >= 1:
                    PurchasedProducts.objects.create(product=product, count=1, user=self.user)
            else:
                print('product already exist')

    def deleteFromPurchasedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if PurchasedProducts.objects.filter(product = product).exists():
                PurchasedProducts.objects.filter(product=product).delete()
    
    def getLikedList(self):
        return self.likedList
    
    def appendTokedList(self, productId):
        if productId != 'none':                
            if LikedProducts.objects.filter(product = Flower.objects.get(pk=productId)).exists() == False:
                product = Flower.objects.get(pk=productId)
                if product.count >= 1:
                    LikedProducts.objects.create(product=product, user=self.user)
            else:
                print('product already exist')

    def deleteFromkedList(self, productId):
        if productId != 'none': 
            product = Flower.objects.get(pk=productId)
            if LikedProducts.objects.filter(product = product).exists():
                LikedProducts.objects.filter(product=product).delete()