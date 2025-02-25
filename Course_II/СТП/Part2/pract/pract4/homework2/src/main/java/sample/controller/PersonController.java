package sample.controller;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import sample.Main;
import sample.models.Person;
import sample.utils.DateUtil;
import sample.utils.PersonGenerator;
import sample.utils.RestApi;

public class PersonController {
    @FXML
    private TableView<Person> personTable;
    @FXML
    private TableColumn<Person, String> firstNameColumn;
    @FXML
    private TableColumn<Person, String> lastNameColumn;

    @FXML
    private Label firstNameLabel;
    @FXML
    private Label lastNameLabel;
    @FXML
    private Label cityLabel;
    @FXML
    private Label streetLabel;
    @FXML
    private Label birthdayLabel;
    @FXML
    private Label postalCodeLabel;

    private Main mainApp;
    private RestApi myApiSession;

    public PersonController() {
    }

    @FXML
    private void initialize() {
        firstNameColumn.setCellValueFactory(cellData -> cellData.getValue().getFirstNameProperty());
        lastNameColumn.setCellValueFactory(cellData -> cellData.getValue().getLastNameProperty());

        showPersonDetails(null);

        personTable.getSelectionModel().selectedItemProperty().addListener(
                ((observableValue, oldValue, newValue) -> showPersonDetails(newValue))
        );
    }

    @FXML
    private void handleDeleteAction() {
        int selectedIndex = personTable.getSelectionModel().getSelectedIndex();
        if (selectedIndex >= 0) {
            Person currentPerson = personTable.getItems().get(selectedIndex);
            if (myApiSession.deletePerson(currentPerson)) {
                personTable.getItems().remove(selectedIndex);
            }

        } else {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.initOwner(mainApp.getPrimaryStage());
            alert.setTitle("ОШИБКА");
            alert.setHeaderText("Пользователи не выбраны");
            alert.setContentText("Пожалуйста выберите пользователя");

            alert.showAndWait();
        }
    }

    private void showPersonDetails(Person person) {
        if (person != null) {
            firstNameLabel.setText(person.getFirstName());
            lastNameLabel.setText(person.getLastName());
            streetLabel.setText(person.getStreet());
            cityLabel.setText(person.getCity());
            birthdayLabel.setText(DateUtil.format(person.getBirthday()));
            postalCodeLabel.setText(Integer.toString(person.getPostalCode()));
        } else {
            firstNameLabel.setText("");
            lastNameLabel.setText("");
            streetLabel.setText("");
            cityLabel.setText("");
            birthdayLabel.setText("");
            postalCodeLabel.setText("");

        }
    }

    public void setMainApp(Main mainApp) {
        this.mainApp = mainApp;
        this.myApiSession = mainApp.getApiSession();
        personTable.setItems(mainApp.getPersonData());
    }

    @FXML
    private void handleNewPerson() {
        PersonGenerator gen = new PersonGenerator();
        Person tmp = new Person(gen.getFirstName(), gen.getLastName(), gen.getStreet(), gen.getCity(), gen.getPostalCode(), gen.getDate());
        //Добавляем персону в СУБД
        myApiSession.CreatePerson(tmp);
        //Обновление данных в таблице
        mainApp.UpdateTable();

    }

    @FXML
    private void editPersonData() {

        int selectedIndex = personTable.getSelectionModel().getSelectedIndex();
        if (selectedIndex >= 0) {
            Person buf = personTable.getItems().get(selectedIndex);
            mainApp.showPersonEditDialog(buf);
        } else {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.initOwner(mainApp.getPrimaryStage());
            alert.setTitle("ОШИБКА");
            alert.setHeaderText("Пользователи не выбраны");
            alert.setContentText("Пожалуйста выберите пользователя");

            alert.showAndWait();
        }
    }
}
