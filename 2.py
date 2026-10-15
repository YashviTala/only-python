import java.util.Scanner;

class Minimum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a <= b && a <= c)
            System.out.println(a);
        else if (b <= a && b <= c)
            System.out.println(b);
        else
            System.out.println(c);
    }
}

 class Arithmetic {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);

        System.out.println("Addition = " + (a + b));
        System.out.println("Subtraction = " + (a - b));
        System.out.println("Multiplication = " + (a * b));
        System.out.println("Division = " + (a / b));
    }
}
[10:03 PM, 10/15/2026] yashvitala: class Employee {
    int age;
    String name;
    float salary;

    public static void main(String[] args) {
        Employee e = new Employee();

        e.age = 20;
        e.name = "Radha";
        e.salary = 25000;

        System.out.println(e.age);
        System.out.println(e.name);
        System.out.println(e.salary);
    }
}
[10:03 PM, 10/15/2026] yashvitala: class Calculate {
    int add(int a, int b) {
        return a + b;
    }

    float add(float a, float b) {
        return a + b;
    }

    String add(String a, String b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculate c = new Calculate();

        System.out.println(c.add(10, 20));
        System.out.println(c.add(2.5f, 3.5f));
        System.out.println(c.add("Hello ", "Java"));
    }
}

[10:04 PM, 10/15/2026] yashvitala: class ExceptionDemo {
    public static void main(String[] args) {
        int arr[] = new int[2];

        try {
            arr[3] = 30 / 0;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Error");
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Error");
        }
    }
}
[10:04 PM, 10/15/2026] yashvitala: class AddSub {
    int num1 = 20, num2 = 10;

    void calAdd() {
        System.out.println(num1 + num2);
    }

    void calSub() {
        System.out.println(num1 - num2);
    }
}

class MulDiv extends AddSub {
    void calMul() {
        System.out.println(num1 * num2);
    }

    void calDiv() {
        System.out.println(num1 / num2);
    }

    public static void main(String[] args) {
        MulDiv m = new MulDiv();

        m.calAdd();
        m.calSub();
        m.calMul();
        m.calDiv();
    }
}

[10:04 PM, 10/15/2026] yashvitala: class TestThread extends Thread {
    public void run() {
        try {
            for (int i = 1; i <= 3; i++) {
                System.out.println(i);
                Thread.sleep(1000);
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        TestThread t1 = new TestThread();
        TestThread t2 = new TestThread();

        t1.start();
        t2.start();
    }
}
[10:04 PM, 10/15/2026] yashvitala: class SleepDemo extends Thread {
    public void run() {
        try {
            System.out.println("Hello");
            Thread.sleep(2000);
            System.out.println("Java");
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        SleepDemo t = new SleepDemo();
        t.start();
    }
}
[10:04 PM, 10/15/2026] yashvitala: import java.io.*;

class ReadFile {
    public static void main(String[] args) throws Exception {
        FileInputStream f = new FileInputStream("abc.txt");

        int i;
        while ((i = f.read()) != -1) {
            System.out.print((char)i);
        }

        f.close();
    }
}

interface Printable {
    void print();
}

interface Showable {
    void show();
}

class Test_Multiple implements Printable, Showable {
    public void print() {
        System.out.println("Print method");
    }

    public void show() {
        System.out.println("Show method");
    }

    public static void main(String[] args) {
        Test_Multiple t = new Test_Multiple();
        t.print();
        t.show();
    }
}