package com.demka;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

class ConnectionDB {

    private Connection con;
    private final String url;
    private final String user;
    private final String password;

    public ConnectionDB(Connection con, String url, String user, String password) {
        this.con = con;
        this.url = url;
        this.user = user;
        this.password = password;
    }

    public Connection getConnection() throws SQLException {
        con = DriverManager.getConnection(url, user, password);
        System.out.println("Подключились к БД");
        return con;
    }

    public void closeConnection() throws SQLException {
        con.close();
        if (con.isClosed()) {
            System.out.println("Дисконнескт");
        }
    }
}

public class Main {

    public static void main(String[] args) throws SQLException, InterruptedException {
        String url = "jdbc:mysql://127.0.0.1:3306/JavaDB";
        String user = "root";
        String password = "tiger";

        //С помощью DriverManager
        Connection connection = DriverManager.getConnection(url, user, password);
        ConnectionDB connectionDB = new ConnectionDB(connection, url, user, password);
        connection = connectionDB.getConnection();
        Thread.sleep(2000);
        connectionDB.closeConnection();

        //TODO соединение с помощью DataSource

    }
}
