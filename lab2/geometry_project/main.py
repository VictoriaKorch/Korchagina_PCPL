#!/usr/bin/env python3
"""
Основной файл программы для тестирования классов с визуализацией
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
from lab_python_oop.rectangle import Rectangle as GeoRectangle
from lab_python_oop.circle import Circle as GeoCircle
from lab_python_oop.square import Square as GeoSquare

def demonstrate_matplotlib():
    """Демонстрация работы с внешним пакетом matplotlib"""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ВНЕШНЕГО ПАКЕТА MATPLOTLIB:")
    print("=" * 60)
    
    try:
        # 1. Создание фигуры и осей
        print("1. Создание графической фигуры...")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # 2. Демонстрация различных возможностей matplotlib
        print("2. Построение геометрических фигур...")
        
        # Левая панель - наши фигуры с размерами N=11
        # Прямоугольник 11x11
        rect = patches.Rectangle((1, 1), 11, 11, linewidth=2, edgecolor='blue', 
                               facecolor='lightblue', alpha=0.7, label='Прямоугольник 11x11')
        ax1.add_patch(rect)
        
        # Круг радиусом 11
        circle = patches.Circle((25, 7), 11, linewidth=2, edgecolor='green',
                              facecolor='lightgreen', alpha=0.7, label='Круг R=11')
        ax1.add_patch(circle)
        
        # Квадрат со стороной 11
        square = patches.Rectangle((40, 1), 11, 11, linewidth=2, edgecolor='red',
                                 facecolor='lightcoral', alpha=0.7, label='Квадрат 11x11')
        ax1.add_patch(square)
        
        # Настройка левой панели
        ax1.set_xlim(0, 55)
        ax1.set_ylim(0, 20)
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Геометрические фигуры (N=11)', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.set_xlabel('X координата')
        ax1.set_ylabel('Y координата')
        
        # 3. Правая панель - математические графики
        print("3. Построение математических графиков...")
        
        # Синусоида с амплитудой 11
        x = np.linspace(0, 4 * np.pi, 100)
        y1 = 11 * np.sin(x)  # Амплитуда = 11
        y2 = 11 * np.cos(x)  # Амплитуда = 11
        
        ax2.plot(x, y1, 'b-', linewidth=2, label='11*sin(x)')
        ax2.plot(x, y2, 'r--', linewidth=2, label='11*cos(x)')
        ax2.fill_between(x, y1, y2, alpha=0.3, color='green')
        
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Тригонометрические функции (Амплитуда=11)', fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.set_xlabel('x')
        ax2.set_ylabel('f(x)')
        
        # 4. Добавление текстовой информации
        fig.suptitle('Демонстрация пакета matplotlib для визуализации (N=11)', 
                    fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        
        # 5. Сохранение графика в файл
        print("4. Сохранение графика в файл...")
        plt.savefig('geometry_plot_N11.png', dpi=300, bbox_inches='tight')
        
        # 6. Показ информации о пакете
        print("5. Информация о пакете matplotlib:")
        print(f"   Версия matplotlib: {plt.__version__}")
        print(f"   Backend: {plt.get_backend()}")
        
        # 7. Показ графика
        print("6. Отображение графика...")
        plt.show()
        
        print("\n✅ Все методы пакета matplotlib работают корректно!")
        print("📊 График сохранен как 'geometry_plot_N11.png'")
        
    except ImportError as e:
        print(f"❌ Ошибка импорта matplotlib: {e}")
    except Exception as e:
        print(f"❌ Ошибка при работе с matplotlib: {e}")

def create_individual_figures():
    """Создание отдельных графиков для каждой фигуры"""
    print("\n" + "=" * 50)
    print("ИНДИВИДУАЛЬНЫЕ ГРАФИКИ ДЛЯ КАЖДОЙ ФИГУРЫ:")
    print("=" * 50)
    
    try:
        # Создаем 3 отдельных графика
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Прямоугольник 11x11
        rect = patches.Rectangle((0.1, 0.1), 0.8, 0.8, 
                               edgecolor='blue', facecolor='lightblue', 
                               linewidth=3, alpha=0.8)
        axes[0].add_patch(rect)
        axes[0].set_xlim(0, 1)
        axes[0].set_ylim(0, 1)
        axes[0].set_aspect('equal')
        axes[0].set_title('Прямоугольник 11x11', fontsize=12, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        axes[0].text(0.5, 0.5, '11x11', ha='center', va='center', fontweight='bold')
        
        # Круг радиусом 11
        circle = patches.Circle((0.5, 0.5), 0.4, 
                              edgecolor='green', facecolor='lightgreen', 
                              linewidth=3, alpha=0.8)
        axes[1].add_patch(circle)
        axes[1].set_xlim(0, 1)
        axes[1].set_ylim(0, 1)
        axes[1].set_aspect('equal')
        axes[1].set_title('Круг R=11', fontsize=12, fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        axes[1].text(0.5, 0.5, 'R=11', ha='center', va='center', fontweight='bold')
        
        # Квадрат со стороной 11
        square = patches.Rectangle((0.1, 0.1), 0.8, 0.8, 
                                 edgecolor='red', facecolor='lightcoral', 
                                 linewidth=3, alpha=0.8)
        axes[2].add_patch(square)
        axes[2].set_xlim(0, 1)
        axes[2].set_ylim(0, 1)
        axes[2].set_aspect('equal')
        axes[2].set_title('Квадрат 11x11', fontsize=12, fontweight='bold')
        axes[2].grid(True, alpha=0.3)
        axes[2].text(0.5, 0.5, '11x11', ha='center', va='center', fontweight='bold')
        
        plt.suptitle('Визуализация геометрических фигур с помощью matplotlib (N=11)', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('individual_figures_N11.png', dpi=300, bbox_inches='tight')
        
        print("📸 Индивидуальные графики сохранены как 'individual_figures_N11.png'")
        
    except Exception as e:
        print(f"❌ Ошибка при создании индивидуальных графиков: {e}")

def main():
    # Номер варианта
    N = 11
    
    print("ДЕМОНСТРАЦИЯ РАБОТЫ С ГЕОМЕТРИЧЕСКИМИ ФИГУРАМИ (N=11):")
    print("=" * 60)
    
    # Создание объектов наших классов
    rectangle = GeoRectangle(N, N, "синий")
    circle = GeoCircle(N, "зеленый")
    square = GeoSquare(N, "красный")
    
    # Вывод информации о фигурах
    print(rectangle)
    print(circle)
    print(square)
    
    # Вывод расчетов площадей
    print(f"\n📐 РАСЧЕТЫ ПЛОЩАДЕЙ (N={N}):")
    print(f"   Прямоугольник {N}x{N}: {N} * {N} = {N*N}")
    print(f"   Круг R={N}: π * {N}² = {3.14159 * N * N:.2f}")
    print(f"   Квадрат {N}x{N}: {N} * {N} = {N*N}")
    
    # Демонстрация работы внешнего пакета matplotlib
    demonstrate_matplotlib()
    
    # Дополнительная демонстрация
    create_individual_figures()

if __name__ == "__main__":
    main()