import java.util.ArrayList;

public class ArrayListEx {

    public static void main(String[] a) {

        //Creating a string array List
        ArrayList<String> arrayL = new ArrayList<String>();
        arrayL.add("Cat");
        arrayL.add("Car");
        arrayL.add("Brother");
        arrayL.add("Basket ball");

        System.out.println("\nThis is String ArrayList size of: "+arrayL.size()+"\n");

        for(int i=0;i<arrayL.size();i++){
            System.out.println(arrayL.get(i));   
        }

        System.out.println("\n=========================\n");

        //creating a Array list of students

        ArrayList<Student> studentList = new ArrayList<Student>();

        Student s1=new Student();
        s1.setName("John");
        s1.setAge(20);
        s1.setSchool("Harvard");
        s1.setMarks(88.9);

        Student s2=new Student();
        s2.setName("Bella");
        s2.setAge(22);
        s2.setSchool("Oxford");
        s2.setMarks(56.9);

        studentList.add(s1);
        studentList.add(s2);

        System.out.println("\nThis is Student ArrayList size of: "+studentList.size()+"\n");

         for(int i=0;i<studentList.size();i++){
            int temp=i+1;
            System.out.println("Details of Student "+temp);
            System.out.println("Name: "+studentList.get(i).getName());
            System.out.println("Age: "+studentList.get(i).getAge());
            System.out.println("School: "+studentList.get(i).getSchool());
            System.out.println("Marks: "+studentList.get(i).getMarks());
            System.out.println("---------------------------\n");
        }

    }
}

//Class of Student
class Student
{
    String name;
    int age;
    String school;
    double marks;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public double getMarks() {
        return marks;
    }

    public void setMarks(double marks) {
        this.marks = marks;
    }
}

