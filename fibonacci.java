import java.util.Scanner;

public class fibonacci {

 public static void main(String[] args) {

  int a = 0, b = 1, c = 0;
  int i, j;
  Scanner sc = new Scanner(System.in);

  System.out.println("Introduce la cantidad de números de la sucesión que quieres que se muestre:");
  i = sc.nextInt();

  System.out.print(a + ", " + b + ", ");

  for (j = 1; j <= i; j++) {

   c = a + b;
   a = b;
   b = c;

   System.out.print(c + ", ");

  }

  sc.close();

 }

}
