import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UserProcessing {
    private static Map<Integer, User> AllUsersMap = new HashMap<>();

    public static Map<Integer, User> getAllUsersMap() {
        return AllUsersMap;
    }

    /**
     * Возвращаем список пользовтаелей по полу
     *
     * @param inputSex
     * @return
     */
    public List<User> getUsers(Sex inputSex) {
        List<User> resultList = new ArrayList<>();
        for (User user : AllUsersMap.values()) {
            if (user.getSex().equals(inputSex)) {
                resultList.add(user);
            }
        }
        return resultList;
    }

    /**
     * Возвращаем список всехх пользователей
     *
     * @return
     */
    public List<User> getUsers() {
        System.out.println(AllUsersMap.values());
        return new ArrayList<User>(AllUsersMap.values());
    }

    /**
     * Возвращаем кол-во пользователей
     *
     * @return
     */
    public int getUsersCount() {
        return AllUsersMap.size();
    }

    /**
     * Возвращаем кол-во пользователей по полу
     *
     * @return
     */
    public int getUsersCount(Sex inputSex) {
        return getUsers(inputSex).size();
    }

    /**
     * Подсчет среднего возраста из общего списка
     *
     * @return
     */
    public double getUsersMiddleAge() {
        long ageSum = 0;
        for (User user : AllUsersMap.values())
            ageSum += user.getAge();

        return (double) ageSum / AllUsersMap.size();
    }

    /**
     * Подсчет среднего возраста по полу
     *
     * @return
     */
    public double getUsersMiddleAge(Sex inputSex) {
        long ageSum = 0;
        int counter = 0;
        for (User user : AllUsersMap.values()) {
            if (user.getSex().equals(inputSex)) {
                ageSum += user.getAge();
                counter++;
            }
        }
        return (double) ageSum / counter;
    }

    /**
     * Сравнение двух пользователей
     *
     * @param firstUser
     * @param secondUser
     * @return
     */
    public boolean equals(User firstUser, User secondUser) {
        return firstUser.equals(secondUser);
    }
}
