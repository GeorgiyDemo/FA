package sample.controller;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import sample.models.Person;
import sample.utils.DateUtil;

import java.util.Date;

public class PersonEditDialog {
    @FXML
    private TextField firstNameField;
    @FXML
    private TextField lastNameField;
    @FXML
    private TextField streetField;
    @FXML
    private TextField cityField;
    @FXML
    private TextField postalCodeField;
    @FXML
    private TextField birthdayField;

    private Stage dialogStage;
    private Person person;
    private boolean okClicked = false;

    @FXML
    private void initialize(){

    }

    public void setDialogStage(Stage dialogStage) {
        this.dialogStage = dialogStage;
    }

    public void setPerson(Person person){
        this.person = person;

        firstNameField.setText(person.getFirstName());
        lastNameField.setText(person.getLastName());
        streetField.setText(person.getStreet());
        cityField.setText(person.getCity());
        postalCodeField.setText(Integer.toString(person.getPostalCode()));
        birthdayField.setText(DateUtil.format(person.getBirthday()));
        birthdayField.setPromptText("dd.mm.yyyy");

    }

    public boolean isOkClicked(){
        return okClicked;
    }

    @FXML
    private void handleCancel(){
        dialogStage.close();
    }

    @FXML
    private void handleOk(){
        if(isInputValid()){

            person.setBirthday(DateUtil.parse(birthdayField.toString()));
            person.setCity(cityField.getText());
            person.setFirstName(firstNameField.getText());
            person.setLastName(lastNameField.getText());
            person.setStreet(streetField.getText());
            person.setPostalCode(postalCodeField.getText());

            okClicked = true;
            dialogStage.close();
        }
    }

    private boolean isInputValid(){
        String errorMessage = "";
        if(firstNameField.getText() == null || firstNameField.getText().length() == 0){
            errorMessage += "Не валидно имя\n";
        }
        if(lastNameField.getText() == null || lastNameField.getText().length() == 0){
            errorMessage += "Не валидна фамилия\n";
        }
        if(streetField.getText() == null || streetField.getText().length() == 0){
            errorMessage += "Не валидна улица\n";
        }
        if(cityField.getText() == null || cityField.getText().length() == 0){
            errorMessage += "Не валиден город\n";
        }

        if(birthdayField.getText() == null || birthdayField.getText().length() == 0){
            errorMessage += "Не введена дата рождения\n";
        }else{
            if(!DateUtil.isValid(birthdayField.getText())){
                errorMessage += "Введите дату в формате dd.MM.yyyy\n";
            }
        }
        if(postalCodeField.getText() == null || postalCodeField.getText().length() == 0){
            errorMessage += "Не введен почтовый индекс\n";
        }else{
            try{
                Integer.parseInt(postalCodeField.getText());
            } catch (NumberFormatException e){
                errorMessage += "Почтовый индекс состоит из цифр";
            }
        }

        if(errorMessage.length() == 0){
            return true;
        }else{
            //TODO:ALERT
            return false;
        }
    }
}
