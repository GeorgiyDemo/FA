package sample;
import javafx.scene.control.Label;
import javafx.fxml.FXML;

public class MainSceneController {

    @FXML
    private Label mainLabel;

    @FXML
    private void buttonHandler() {
        mainLabel.setText("Checked");
        System.out.println("Button clicked!");
    }
}
