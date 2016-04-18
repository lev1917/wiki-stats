#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = (0, 0)
            k=f.readline()
            k=k.rstrip()
            n,_nlinks=map(int, k.split())
            self._titles = []
            print(n, _nlinks)
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))
            for i in range(n):
                title=f.readline()
                title=title.rstrip()
                r=self._offset[i]
                self._titles.append(title)
                g=f.readline()
                g=g.rstrip()
                size, redirect,m=map(int,g.split())
                self._sizes[i]=size
                self._redirect[i]=redirect

                for y in range(m):
                    d=f.readline()
                    d=d.rstrip()
                    d=int(d)
                    self._links[r+y]=d
                self._offset[i+1]=r+m



        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1]-self._offset[_id]

    def get_links_from(self, _id):
        g=self._links[self._offset[_id]:self._offset[_id+1]]
        return g

    def get_id(self, title):
        for i in range(len(self._titles)):
            if self._titles==title:
                return i

    def get_number_of_pages(self):
        return len(self._titles)-self._redirect.count(0)

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        else:
            return False



    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]




def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл



wg = WikiGraph()
wg.load_from_file('wiki_small.txt')
min1=float('+inf')
min_sul=0
print('количество статей с перенаправлением',len(wg._redirect)-wg._redirect.count(0))
for i in range(len(wg._sizes)):
        if wg.get_number_of_links_from(i)==min1:
            min_sul+=1
        if wg.get_number_of_links_from(i)<min1:
            min_sul=1
            min1=wg.get_number_of_links_from(i)


print('минимальное количество ссылок из статьи',min1)
print('Количесво ссылок с минимальным количеством ссылок',min_sul)
min1=float('-inf')
min_sul=0
l=''
print('количество статей с перенаправлением',len(wg._redirect)-wg._redirect.count(0))
for i in range(len(wg._sizes)):
        if wg.get_number_of_links_from(i)==min1:
            min_sul+=1

        if wg.get_number_of_links_from(i)>min1:
            min_sul=1
            min1=wg.get_number_of_links_from(i)
            l=wg.get_title(i)

print('максимальное количество ссылок из статьи',min1)
print('количество статей с максимальным количеством ссылок',min_sul)
print('статья с наибольшим количеством ссылок',l)
sum=0

for i in range(len(wg._sizes)):
    sum+=int(wg.get_number_of_links_from(i))
print('среднее количество ссылок в статье',sum/len(wg._sizes))



min1=float('+inf')
min_sul=0
for i in range(len(wg._sizes)):
        if wg.get_number_of_links_from(i)-wg._redirect[i]==min1:
            min_sul+=1

        if wg.get_number_of_links_from(i)-wg._redirect[i]<min1:
            min_sul=1
            min1=wg.get_number_of_links_from(i)

print('минимальное количество ссылок на статью',min1)
print('количество статей с минимальным количеством внешних ссылок',min_sul)
Pe=max(wg._redirect)
l=''
suM=0
for i in range(len(wg._redirect)):
    if wg._redirect[i]==Pe:
        l=wg.get_title(i)
        suM+=1
Sum=0
for i in range(len(wg._redirect)):
    Sum+=wg._redirect[i]
print('среднее количество внешних перенаправлений на статью',Sum/len(wg._redirect))
