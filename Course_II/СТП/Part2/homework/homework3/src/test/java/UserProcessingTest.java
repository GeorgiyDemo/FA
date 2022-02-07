import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class UserProcessingTest {

    @Test
    public void getAllMaleUsers() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        List<User> actual = userProcessing.getUsers(Sex.MALE);

        List<User> expected = new ArrayList<>();
        expected.add(user1);
        expected.add(user2);

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getAllFemaleUsers() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        List<User> actual = userProcessing.getUsers(Sex.FEMALE);

        List<User> expected = new ArrayList<>();
        expected.add(user3);

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testGetAllUsers() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();

        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        List<User> actual = userProcessing.getUsers();

        List<User> expected = new ArrayList<>();
        expected.add(user1);
        expected.add(user2);
        expected.add(user3);

        Assert.assertEquals(expected, actual);

    }

    @Test
    public void getAllUsersCount() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        int actual = userProcessing.getUsersCount();
        int expected = 3;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getMaleUsersCount() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        int actual = userProcessing.getUsersCount(Sex.MALE);
        int expected = 2;

        Assert.assertEquals(expected, actual);
    }


    @Test
    public void getFemaleUsersCount() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);

        int actual = userProcessing.getUsersCount(Sex.FEMALE);
        int expected = 1;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testAllUsersMiddleAge() {

        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user4 = new User(4, "Екатерина", 18, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);
        userProcessing.getAllUsersMap().put(user4.getId(), user4);

        double actual = userProcessing.getUsersMiddleAge();
        double expected = 21.25;

        Assert.assertEquals(expected, actual, 0.0001);

    }

    @Test
    public void testMaleUsersMiddleAge() {
        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user4 = new User(4, "Екатерина", 18, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);
        userProcessing.getAllUsersMap().put(user4.getId(), user4);

        double actual = userProcessing.getUsersMiddleAge(Sex.MALE);
        double expected = 18;

        Assert.assertEquals(expected, actual, 0.0001);
    }

    @Test
    public void testFemaleUsersMiddleAge() {
        User user1 = new User(1, "Алексей", 22, Sex.MALE);
        User user2 = new User(2, "Николай", 14, Sex.MALE);
        User user3 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user4 = new User(4, "Екатерина", 18, Sex.FEMALE);

        UserProcessing userProcessing = new UserProcessing();
        userProcessing.getAllUsersMap().put(user1.getId(), user1);
        userProcessing.getAllUsersMap().put(user2.getId(), user2);
        userProcessing.getAllUsersMap().put(user3.getId(), user3);
        userProcessing.getAllUsersMap().put(user4.getId(), user4);

        double actual = userProcessing.getUsersMiddleAge(Sex.FEMALE);
        double expected = 24.5;
        Assert.assertEquals(expected, actual, 0.0001);
    }

    @Test
    public void testEqualsTrue() {

        UserProcessing userProcessing = new UserProcessing();

        User user1 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user2 = new User(4, "Алиса", 31, Sex.FEMALE);

        boolean actual = userProcessing.equals(user1, user2);
        boolean expected = true;
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testEqualsFalse() {

        UserProcessing userProcessing = new UserProcessing();

        User user1 = new User(3, "Алиса", 31, Sex.FEMALE);
        User user2 = new User(4, "Алиса", 32, Sex.FEMALE);

        boolean actual = userProcessing.equals(user1, user2);
        boolean expected = false;
        Assert.assertEquals(expected, actual);
    }
}