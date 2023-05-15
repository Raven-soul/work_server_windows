from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

import random

class Detail_page(object):
    def __init__(self, prod_id, request):
        self.startBuilder(prod_id, request)

        script_list = [{'script_url':'flower/js/detail.js'}]

        self.header.setData(name = 'content_style_path', value = 'flower/css/content/detail_content.css')
        self.footer.setData(name = 'script_list', value = script_list)

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'product': self.productItem,
            'reviews': self.getReviews(self.productItem),
            'composition': self.compositionFormer(self.productItem),
            'like_block': self.likedFormer(self.productList)
        }

    def startBuilder(self, prod_id, request):
        self.header = Header(request)
        self.footer = Footer()

        self.productList = Flower.objects.all()
        self.productItem = Flower.objects.get(pk=prod_id)

    def getDict(self):
        return self.context
            
    def getReviews(self, productItem):
        reviews = Review.objects.all()
        temp_result = {'global_grade': 0, 'global_stars': '', 'number_all_reviews' : 0, 'few_reviews': ''}
        temp_reviews = []
        grades = []

        for item in reviews:
            if item.flower.pk == productItem.pk:
                temp_reviews.append({'grade': item.grade, 'stars':{'fill': [0 for i in range(item.grade)], 'less': [0 for i in range(5-item.grade)]}, 'author': item.author, 'description': item.description})
                grades.append(item.grade)
        
        
        if temp_reviews == []:
            temp_result['few_reviews'] = ''  
            temp_result['global_stars'] = {'fill': [], 'less': [0 for i in range(5)]}  
        else:
            average = sum(grades)/len(grades)
            temp_result['global_grade'] = average
            temp_result['global_stars'] = {'fill': [0 for i in range(round(average))], 'less': [0 for i in range(5-round(average))]}
            temp_result['number_all_reviews'] = len(temp_reviews)
            temp_result['few_reviews'] = temp_reviews # TODO нужно сократить выгрузку до 3-4 отзывов
            

        return temp_result
    
    def compositionFormer(self, productItem):
        composition = Composition.objects.all()
        wrapping = Wrapping.objects.all()
        temp_result = {'product': 'none', 'wrapping': 'none'}

        for comp in composition:
            if comp.flower.pk == productItem.pk:
                temp_result['product'] = {'part_1': comp.flower_part_1, 'part_2': comp.flower_part_2, 'part_3': comp.flower_part_3}

        for wrap in wrapping:
            if wrap.flower.pk == productItem.pk:
                temp_result['wrapping'] = {'part_1': wrap.wrapping_part_1, 'part_2': wrap.wrapping_part_2}

        return temp_result
    
    def likedFormer(self, productList):
        temp_result = []

        for elem in range(4):
            random_element = random.choice(productList)
            temp_result.append({'name': random_element.title, 'path': random_element.get_absolute_url, 'photo':random_element.photo, 'price': random_element.price})

        return temp_result


