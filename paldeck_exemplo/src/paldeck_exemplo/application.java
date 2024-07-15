package paldeck_exemplo;

import java.util.Locale;
import java.util.Scanner;

public class application {

	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		Locale.setDefault(Locale.US);
		
		System.out.println("Digite seu nome: ");
		String nome = sc.next();
		System.out.println("Bem vindo a sua Paldeck: " + nome);
		System.out.println("Cadastrar novo Pal: ");
		System.out.println();
		System.out.println("Entre com o nome do Pal: ");
		String palNome = sc.next();
		System.out.println("Habilidade: ");
		String habilidade = sc.next();
		
		System.out.println("Paldeck de: " + nome + "\n Nome do Pal: " + palNome + "\n Habilidade: " + habilidade);
		
		
		sc.close();
	}

}
