import java.io.*;

class WriteFile {
    public static void main(String[] args) throws Exception {
        FileOutputStream f = new FileOutputStream("abc.txt");

        String s = "Hello Java";
        f.write(s.getBytes());

        f.close();
        System.out.println("Data Written");
    }
}

import java.io.*;

class ReadFile {
    public static void main(String[] args) throws Exception {
        FileReader f = new FileReader("abc.txt");

        int i;
        while ((i = f.read()) != -1) {
            System.out.print((char)i);
        }

        f.close();
    }
}

import java.io.*;

class CopyFile {
    public static void main(String[] args) throws Exception {
        FileInputStream f1 = new FileInputStream("abc.txt");
        FileOutputStream f2 = new FileOutputStream("xyz.txt");

        int i;
        while ((i = f1.read()) != -1) {
            f2.write(i);
        }

        f1.close();
        f2.close();

        System.out.println("File Copied");
    }
}


import java.sql.*;

class CreateTable {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");

        Connection c = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/employee",
            "root", ""
        );

        Statement s = c.createStatement();

        s.executeUpdate(
            "CREATE TABLE emp (emp_id INT(5), emp_name VARCHAR(10))"
        );

        System.out.println("Table Created");
        c.close();
    }
}

import java.sql.*;

class InsertData {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");

        Connection c = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/employee",
            "root", ""
        );

        Statement s = c.createStatement();

        s.executeUpdate(
            "INSERT INTO emp VALUES (101, 'radha'), (102, 'kanha')"
        );

        System.out.println("Records Inserted");
        c.close();
    }
}