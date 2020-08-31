import java.util.*;

 // Compiler version JDK 11.0.2

 class Covid19Checkup
 {
   public static void main(String args[])
   {
    int ara[] = new int[10];
         String name;

         Scanner sc = new Scanner(System.in);
         System.out.println("COVID-19 Checkup Java program");

         System.out.println("Please enter your name");
         name = sc.nextLine();
         System.out.println("What is your age?\n");
         ara[0] = sc.nextInt();
         System.out.println("Dear "+name+", Do you have fever?\nYes=0,No=1\n");
         ara[1] = sc.nextInt();
         System.out.println("Do you have respiratory distress?\nYes=0,No=1\n");
         ara[2] = sc.nextInt();
         System.out.println("Do you have cough?\nYes=0,No=1\n");
         ara[3] = sc.nextInt();
         System.out.println("Do you feel tired?\nYes=0,No=1\n");
         ara[4] = sc.nextInt();

             if(ara[1]==0 && ara[2]==0 && ara[3]==0 && ara[4]==0)
    {
        System.out.println("Dear "+name+",\nYou should go to the clinic and test your blood.\n ");

    }

    else {

        System.out.println("Dear "+name+", If you feel very sick,Go to the clinic.\n");
   }

   System.out.println("According to www.worldometer.info,");

   if(ara[0]>=0 && ara[0]<=9){

      System.out.println("\nIn your age fatality rate of corona virus is 0.00%");
   }

   else if(ara[0]>=10 && ara[0]<=19){
      System.out.println("\nIn your age fatality rate of corona virus is 0.2%");

   }

   else if(ara[0]>=20 && ara[0]<=29){
      System.out.println("\nIn your age fatality rate of corona virus is 0.2%");
      }

   else if(ara[0]>=30 && ara[0]<= 39){
     System.out.println("\nIn your age fatality rate of corona virus is 0.2%");

   }

   else if(ara[0]>=40 && ara[0]<=49){
     System.out.println("\nIn your age fatality rate of corona virus is 0.4%");


   }

   else if(ara[0]>=50 && ara[0]<=59){
     System.out.println("\nIn your age fatality rate of corona virus is 1.3%");

   }

   else if(ara[0]>=60 && ara[0]<=69){
     System.out.println("\nIn your age fatality rate of corona virus is 3.6%");

   }

   else if(ara[0]>=70 && ara[0]<=79){
     System.out.println("\nIn your age fatality rate of corona virus is 8.0%");

   }

   else if(ara[0]>=80){
     System.out.println("\nIn your age fatality rate of corona virus is 21.8% or 14.8%");

   }

   System.out.println("\n\n\nImportant tips to prevent it:\n1)Stay at home\n2)Use mask\n3)Wash your hands with soap, \n or use acohol-base rub kills viruses\n  that may be on your hands.\n");
   System.out.println("Thank you....Please give me a star");
   System.out.println("Developed by Dave Enyi");
   }
 }
