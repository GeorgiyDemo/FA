public class App {

    public static void main(String[] args) {

        UserProcessing userProcessing = new UserProcessing();

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user4 = new User(4, "Екатерина", 18, Sex.FEMALE);

        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);
        userProcessing.getAllUsersMap().put(user4.getId(), user4);

        for (User user : userProcessing.getUsers()) {
            System.out.println(user);
        }

    }
}
