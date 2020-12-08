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
                "jdbc:mysql://localhost:3306/JavaDB",
                "root", "tiger", 2);
        try {
            conn = pool.getConnection();
            try (Statement statement = conn.createStatement())
            {
                ResultSet res = statement.executeQuery("show tables");
                System.out.println("There are below tables:");
                while (res.next()) {
                    String tblName = res.getString(1);
                    System.out.println(tblName);
                }
            }
        }
        finally {
            if (conn != null) {
                pool.returnConnection(conn);
            }
        }
    }

}
