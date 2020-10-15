using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace koh
{
    public partial class Form1 : Form
    {
        
        static Pen pen1;
        static Graphics g;
        static Pen pen2;
        

        public Form1()
        {
            InitializeComponent();
        }
  
        private void Draw(object sender, EventArgs e)
        {
            //Выбираем цвета зарисовки 
            pen1 = new Pen(Color.Green, 1); 
            pen2 = new Pen(Color.Blue, 1);
            //Объявляем объект "g" класса Graphics
            g = CreateGraphics();
            g.Clear(Color.Black);//Зарисовка экрана черным фоном
 
            //Определим коорднаты исходного треугольника
            var point1 = new PointF(200, 200);
            var point2 = new PointF(500, 200);
            var point3 = new PointF(350, 400);

            //Зарисуем треугольник
            g.DrawLine(pen1, point1, point2);
            g.DrawLine(pen1, point2, point3);
            g.DrawLine(pen1, point3, point1);

            //Вызываем функцию Fractal для того, чтобы
            //нарисовать три кривых Коха на сторонах треугольника
            Fractal(point1, point2, point3, 5);
            Fractal(point2, point3, point1, 5);
            Fractal(point3, point1, point2, 5);
           }


        //рекурсивная функция рисования кривой Коха
        static int Fractal(PointF p1, PointF p2, PointF p3, int iter)
        {
            //n -количество итераций
            if (iter > 0)  //условие выхода из рекурсии
            {
                //средняя треть отрезка
                var p4 = new PointF((p2.X + 2 * p1.X) / 3, (p2.Y + 2 * p1.Y) / 3);
                var p5 = new PointF((2 * p2.X + p1.X) / 3, (p1.Y + 2 * p2.Y) / 3);
                //координаты вершины угла
                var ps = new PointF((p2.X + p1.X) / 2, (p2.Y + p1.Y) / 2);
                var pn = new PointF((4 * ps.X - p3.X) / 3, (4 * ps.Y - p3.Y) / 3);
                //рисуем его
                g.DrawLine(pen1, p4, pn);
                g.DrawLine(pen1, p5, pn);
                g.DrawLine(pen2, p4, p5);

      
                //рекурсивно вызываем функцию нужное число раз
                Fractal(p4, pn, p5, iter - 1);
                Fractal(pn, p5, p4, iter - 1);
                Fractal(p1, p4, new PointF((2 * p1.X + p3.X) / 3, (2 * p1.Y + p3.Y) / 3), iter - 1);
                Fractal(p5, p2, new PointF((2 * p2.X + p3.X) / 3, (2 * p2.Y + p3.Y) / 3), iter - 1);

            }
            return iter;
        }

    }
}
