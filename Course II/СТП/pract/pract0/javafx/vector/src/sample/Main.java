package sample;


import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;


public class Main extends Application  {

    /*
    Обработка нажатия на Button
     */
    public void buttonClick(String data){

        System.out.println(data);

    }

    /*
    GUI
     */
    @Override
    public void start(Stage primaryStage) throws Exception {
        primaryStage.setTitle("Операции над векторами");

        TextField textField = new TextField();
        Button button = new Button("Ввод");
        button.setOnAction(action -> {
            buttonClick(textField.getText());
        });
        Label label = new Label("ПРИМЕР");
        label.setAlignment(Pos.CENTER);

        HBox hbox = new HBox(textField, button, label);


        //Сцена
        Scene scene = new Scene(hbox, 300, 300);
        primaryStage.setScene(scene);
        primaryStage.show();




    }

    public static void main(String[] args) {
        Application.launch(args);
    }

}