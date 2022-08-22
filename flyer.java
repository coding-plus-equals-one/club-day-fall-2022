class Main {
    public static void codingClubPitch(boolean coding){
        if (!coding) {
            System.out.println("Don't worry, no experience is needed.");
            // coding += 1
            coding = true;
            codingClubPitch(coding);
        } else {
            System.out.println("Join the coding club!");
            System.out.println("Thurs and Fri in Room 752.");
            System.exit(0);
        }
    }   
    public static void main(String[] args){
        boolean coding = false;
        codingClubPitch(coding);
    }
}