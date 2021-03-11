package sample.utils;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import sample.models.Person;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class RestApi {

    private static final String ServerURL = "http://127.0.0.1:8080";

    /**
     * Создание персоны
     * Использет POST
     * @param person
     */
    public void CreatePerson(Person person){
        HttpClass.PostRequest(ServerURL+"/persons",person.toJson());
    }

    /**
     * Получение персоны по опеределенному id
     * Использет GET
     * @param id
     * @return
     */
    //public Person GetPerson(String id){

    //}

    /**
     * Получение всех персон
     * Использет GET
     * @return
     */
    public List<Person> GetPerson(){
        List<Person> result = new ArrayList<>();
        String buffer = HttpClass.GetRequest(ServerURL+"/persons");

        JsonArray jsonResult = JsonParser.parseString(buffer).getAsJsonArray();

        for (int i = 0; i < jsonResult.size(); i++) {
            JsonObject currentPerson = jsonResult.get(i).getAsJsonObject();

            String firstName = currentPerson.get("firstName").getAsString();
            String lastName = currentPerson.get("lastName").getAsString();
            String street = currentPerson.get("street").getAsString();
            String city = currentPerson.get("city").getAsString();
            Integer postalCode = currentPerson.get("postalCode").getAsInt();
            LocalDate date = LocalDate.parse(currentPerson.get("birthday").getAsString());
            Integer id = currentPerson.get("id").getAsInt();

            Person newPerson = new Person(firstName,lastName,street,city,postalCode, date, id);
            result.add(newPerson);
        }
        return result;
    }

    /**
     * Обновление персоны
     * Использует PUT
     * @param person
     */
    public void updatePerson(Person person){
        Integer id = person.getId();
        String jsonString = person.toJson();
        HttpClass.PutRequest(ServerURL+"/persons/"+id, jsonString);
    }

    /**
     * Удаление персоны.
     * Использует DELETE
     * @param person
     */
    public boolean deletePerson(Person person){
        Integer id = person.getId();
        if (id == null)
            return false;
        return HttpClass.DeleteRequest(ServerURL+"/persons/"+id);
    }
}
