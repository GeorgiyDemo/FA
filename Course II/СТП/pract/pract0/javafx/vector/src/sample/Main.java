package sample;


import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

import java.net.URL;

public class Main extends Application  {

    /*
    GUI
     */
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("./mainScene.fxml"));
        Controller controller = loader.getController();
        Parent root = loader.load();

        primaryStage.setScene(new Scene(root));
        primaryStage.show();
    }

    /*
    Обработка нажатия на Button
     */
    @FXML
    public void buttonClick(String data){
        System.out.println(data);

    }

    public static void main(String[] args) {
        Application.launch(args);
    }

}