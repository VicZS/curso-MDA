public class App {
    public static void main(String[] args) throws Exception {
         // Crear una instancia de Subject (sujeto)
         Subject subject = new Subject();

         // Crear instancias de los clientes (observers)
         Observer cliente1 = new Cliente("Juan");
         Observer cliente2 = new Cliente("María");
         Observer cliente3 = new Cliente("Pedro");
 
         // Registrar los clientes como observadores del sujeto
         subject.registerObserver(cliente1);
         subject.registerObserver(cliente2);
         subject.registerObserver(cliente3);
 
         // Simular un cambio en el producto
         Product nuevoProducto = new Product("iPhone 13", 999.99);
         subject.setNewProduct(nuevoProducto);
 
         // Aquí puedes agregar más lógica o pruebas según tus necesidades
    }
}

