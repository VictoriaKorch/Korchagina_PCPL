import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse

def advanced_plotting_demo():
    """Расширенная демонстрация возможностей matplotlib с N=11"""
    
    print("\n" + "=" * 60)
    print("РАСШИРЕННАЯ ДЕМОНСТРАЦИЯ MATPLOTLIB (N=11)")
    print("=" * 60)
    
    # 1. Создание сложной фигуры с несколькими панелями
    fig = plt.figure(figsize=(15, 10))
    
    N = 11  # Наш параметр
    
    # 2. Различные геометрические фигуры с размерами N=11
    ax1 = fig.add_subplot(231)
    
    # Прямоугольник 11x11
    rect = Rectangle((1, 1), N, N, linewidth=3, edgecolor='blue', 
                   facecolor='lightblue', alpha=0.8, label=f'Прямоугольник {N}x{N}')
    ax1.add_patch(rect)
    
    # Круг радиусом 11
    circle = Circle((25, 8), N, linewidth=3, edgecolor='green',
                  facecolor='lightgreen', alpha=0.8, label=f'Круг R={N}')
    ax1.add_patch(circle)
    
    # Квадрат со стороной 11
    square = Rectangle((42, 1), N, N, linewidth=3, edgecolor='red',
                     facecolor='lightcoral', alpha=0.8, label=f'Квадрат {N}x{N}')
    ax1.add_patch(square)
    
    ax1.set_xlim(0, 55)
    ax1.set_ylim(0, 20)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Основные геометрические фигуры (N=11)')
    ax1.legend()
    
    # 3. Столбчатая диаграмма - сравнение площадей
    ax2 = fig.add_subplot(232)
    categories = [f'Прямоугольник\n{N}x{N}', f'Круг\nR={N}', f'Квадрат\n{N}x{N}']
    rectangle_area = N * N
    circle_area = np.pi * N * N
    square_area = N * N
    areas = [rectangle_area, circle_area, square_area]
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    
    bars = ax2.bar(categories, areas, color=colors, edgecolor=['blue', 'green', 'red'], 
                   linewidth=2, alpha=0.8)
    ax2.set_title('Сравнение площадей фигур (N=11)')
    ax2.set_ylabel('Площадь')
    
    # Добавление значений на столбцы
    for bar, area in zip(bars, areas):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{area:.1f}', ha='center', va='bottom', fontweight='bold')
    
    # 4. Круговая диаграмма
    ax3 = fig.add_subplot(233)
    ax3.pie(areas, labels=categories, colors=colors, autopct='%1.1f%%', 
            startangle=90, explode=(0.1, 0, 0))
    ax3.set_title('Доли площадей фигур (N=11)')
    
    # 5. График математических функций с амплитудой 11
    ax4 = fig.add_subplot(234)
    x = np.linspace(0, 2*np.pi, 100)
    y1 = N * np.sin(x)  # Амплитуда = 11
    y2 = N * np.cos(x)  # Амплитуда = 11
    
    ax4.plot(x, y1, 'b-', label=f'{N}*sin(x)', linewidth=2)
    ax4.plot(x, y2, 'r-', label=f'{N}*cos(x)', linewidth=2)
    ax4.fill_between(x, y1, y2, where=(y1 > y2), color='green', alpha=0.3, label='sin > cos')
    ax4.fill_between(x, y1, y2, where=(y1 <= y2), color='red', alpha=0.3, label='sin ≤ cos')
    ax4.legend()
    ax4.set_title(f'Тригонометрические функции (Амплитуда={N})')
    ax4.grid(True, alpha=0.3)
    
    # 6. Дополнительные геометрические фигуры с размерами, связанными с N=11
    ax5 = fig.add_subplot(235)
    
    # Эллипс с осями 11 и 5.5
    ellipse = Ellipse((8, 8), N, N/2, linewidth=3, edgecolor='purple',
                     facecolor='violet', alpha=0.7, label=f'Эллипс {N}x{N/2}')
    ax5.add_patch(ellipse)
    
    # Треугольник с высотой 11
    triangle = Polygon([[2, 2], [2+N, 2], [2+N/2, 2+N]], linewidth=3,
                     edgecolor='orange', facecolor='yellow', alpha=0.7, label=f'Треугольник h={N}')
    ax5.add_patch(triangle)
    
    # Ромб с диагоналями 11 и 11
    rhombus = Polygon([[15, 5], [15+N/2, 5+N/2], [15, 5+N], [15-N/2, 5+N/2]], linewidth=3,
                     edgecolor='brown', facecolor='pink', alpha=0.7, label=f'Ромб d={N}')
    ax5.add_patch(rhombus)
    
    ax5.set_xlim(0, 25)
    ax5.set_ylim(0, 15)
    ax5.set_aspect('equal')
    ax5.grid(True, alpha=0.3)
    ax5.set_title('Дополнительные фигуры (размеры связаны с N=11)')
    ax5.legend()
    
    # 7. Диаграмма рассеяния с цветовым кодированием
    ax6 = fig.add_subplot(236)
    np.random.seed(42)
    
    # Генерация случайных точек для разных фигур
    n_points = 50
    
    # Точки внутри прямоугольника 11x11
    x_rect = np.random.uniform(1, 1+N, n_points)
    y_rect = np.random.uniform(1, 1+N, n_points)
    
    # Точки внутри круга радиусом 11
    theta = np.random.uniform(0, 2*np.pi, n_points)
    r = np.random.uniform(0, N, n_points)
    x_circle = 25 + r * np.cos(theta)
    y_circle = 8 + r * np.sin(theta)
    
    # Точки внутри квадрата 11x11
    x_square = np.random.uniform(42, 42+N, n_points)
    y_square = np.random.uniform(1, 1+N, n_points)
    
    # Объединяем все точки
    x_all = np.concatenate([x_rect, x_circle, x_square])
    y_all = np.concatenate([y_rect, y_circle, y_square])
    colors_scatter = ['blue'] * n_points + ['green'] * n_points + ['red'] * n_points
    
    scatter = ax6.scatter(x_all, y_all, c=colors_scatter, alpha=0.6, s=30)
    ax6.set_xlim(0, 55)
    ax6.set_ylim(0, 20)
    ax6.set_aspect('equal')
    ax6.set_title('Случайные точки в фигурах (N=11)')
    ax6.grid(True, alpha=0.3)
    
    # Добавляем контуры фигур
    rect_outline = Rectangle((1, 1), N, N, linewidth=2, edgecolor='blue', 
                           facecolor='none', linestyle='--')
    ax6.add_patch(rect_outline)
    
    circle_outline = Circle((25, 8), N, linewidth=2, edgecolor='green',
                          facecolor='none', linestyle='--')
    ax6.add_patch(circle_outline)
    
    square_outline = Rectangle((42, 1), N, N, linewidth=2, edgecolor='red',
                             facecolor='none', linestyle='--')
    ax6.add_patch(square_outline)
    
    plt.suptitle(f'Расширенная демонстрация возможностей matplotlib для геометрии (N={N})', 
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('advanced_plotting_N11.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Вывод информации о площадях
    print(f"\n📊 РАСЧЕТЫ ПЛОЩАДЕЙ ДЛЯ N={N}:")
    print(f"   Прямоугольник {N}x{N}: {N} × {N} = {rectangle_area}")
    print(f"   Круг R={N}: π × {N}² = {circle_area:.2f}")
    print(f"   Квадрат {N}x{N}: {N} × {N} = {square_area}")
    
    print("\n🎨 Расширенная демонстрация завершена!")
    print("📊 График сохранен как 'advanced_plotting_N11.png'")

if __name__ == "__main__":
    advanced_plotting_demo()