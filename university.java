public class university {
    void Educational_organization(){
        System.out.println("Colleges are affiliated");
    }
}

class PSIT extends university{
    void College(){
        System.out.println("Affiliated under university");
    }
}

class main{
    public static void main(String args[]){
        PSIT p = new PSIT();
        university u = new university();
        p.College();
        u.Educational_organization();
    }
}
