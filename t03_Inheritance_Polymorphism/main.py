from figures import *

max_figure = find_max_figure("input01.txt")
print("Найбільша фігура у input01.txt:", type(max_figure).__name__)
print("Міра:", max_figure.volume())

max_figure = find_max_figure("input02.txt")
print("Найбільша фігура у input02.txt:", type(max_figure).__name__)
print("Міра:", max_figure.volume())

max_figure = find_max_figure("input03.txt")
print("Найбільша фігура у input03.txt:", type(max_figure).__name__)
print("Міра:", max_figure.volume())