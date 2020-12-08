package com.demka;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class Main {
    // Just an Example
   public static void main(String[] args) throws SQLException, SQLException {
        Connection conn = null;
        MySQLConnectionPool pool = new MySQLConnectionPool(
                "jdbc:mysql://localhost:3306/JavaDB?characterEncoding=utf-8",
                "root", "tiger", 2);
        try {
            conn = pool.getConnection();
            try (Statement statement = conn.createStatement())
            {
                ResultSet res = statement.executeQuery("show tables");
                System.out.println("Таблицы в БД:");

                while (res.next()) {
                    String tblName = res.getString(1);
                    System.out.println(tblName);
                }

                String SQLString = "INSERT INTO students (first_name,last_name) VALUES('ИМЯ ИМЯ ИМЯ','ФАМИЛИЯ ФАМИЛИЯ ФАМИЛИЯ');";
                boolean resultFlag = statement.execute(SQLString);
                System.out.println("Результат: "+resultFlag);

            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        finally {
            if (conn != null) {
                pool.returnConnection(conn);
            }
        }
    }

}
