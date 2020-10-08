package sample;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

/*
Контроллер MainScene
 */
public class Controller {

    @FXML
    private Label wrongInputLabel;


    /*
    Основной обработчик нажатия на button
     */
    @FXML
    private void mainButtonClick() {
        System.out.println("WORKING");

    }
}
