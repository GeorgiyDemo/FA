import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class User {


    private int id;
    private String name;
    private int age;
    private Sex sex;


    public boolean equals(User otherUser) {
        return (otherUser.getName().equals(this.getName()) && (otherUser.getAge() == this.getAge()) && (otherUser.getSex() == this.getSex()));
    }


    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", sex='" + sex + '\'' +
                '}';
    }
}
