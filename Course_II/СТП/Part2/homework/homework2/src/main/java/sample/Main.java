package sample;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Modality;
import javafx.stage.Stage;
import sample.controller.PersonController;
import sample.controller.PersonEditDialog;
import sample.models.Person;
import sample.utils.PersonGenerator;

import java.io.IOException;

public class Main extends Application {

    public Main(){
        for(int i=0;i<20;i++){
            PersonGenerator gen = new PersonGenerator();
            Person tmpPerson = new Person(gen.getFirstName(), gen.getLastName(), gen.getStreet(), gen.getCity(), gen.getPostalCode(), gen.getDateYear(), gen.getDateMonth(), gen.getDateDayOfMonth());
            personData.add(tmpPerson);
        }
    }
    private Stage primaryStage;
    private BorderPane rootLayout;

    private ObservableList<Person> personData = FXCollections.observableArrayList();

    public Stage getPrimaryStage() {
        return primaryStage;
    }

    public BorderPane getRootLayout() {
        return rootLayout;
    }

    public void initRootLayout(){
        try{
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("/RootLayout.fxml"));
            rootLayout = (BorderPane) loader.load();

            Scene scene = new Scene(rootLayout);
            primaryStage .setScene(scene);
            primaryStage.show();

        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public boolean showPersonEditDialog(Person person){
        try{
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("/personEditDialog.fxml"));
            AnchorPane page = (AnchorPane) loader.load();

            Stage dialogStage = new Stage();
            dialogStage.setTitle("Edit Person");
            dialogStage.initModality(Modality.WINDOW_MODAL);
            dialogStage.initOwner(primaryStage);
            Scene scene = new Scene(page);
            dialogStage.setScene(scene);
            PersonEditDialog controller = loader.getController();
            controller.setDialogStage(dialogStage);
            controller.setPerson(person);
            dialogStage.showAndWait();;
            return controller.isOkClicked();
        }catch(IOException e){
            e.printStackTrace();
            return false;
        }
    }
    public void showPersons(){
        try{
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(getClass().getResource("/main.fxml"));
            AnchorPane persons = (AnchorPane) loader.load();

            rootLayout.setCenter(persons);

            PersonController controller = loader.getController();
            controller.setMainApp(this);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    @Override
    public void start(Stage primaryStage) throws Exception{
        this.primaryStage = primaryStage;
        this.primaryStage.setTitle("ADDRESS");
        initRootLayout();
        showPersons();
    }


    public static void main(String[] args) {
        launch(args);
    }

    public ObservableList<Person> getPersonData() {
        return personData;
    }

    public void setPersonData(Person person){
        personData.add(person);
    }

}
