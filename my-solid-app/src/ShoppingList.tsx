import { createSignal, onMount } from "solid-js";
import axios, { AxiosError } from "axios";  // AxiosError importieren
import styles from "./Style.module.css";

// Definition der Struktur eines Shopping-Items
interface ShoppingItem {
  name: string;
  amount: number;
}

function ShoppingList() {
  // createSignal zum Speichern der geladenen Items
  const [items, setItems] = createSignal<ShoppingItem[]>([]);
  const [loading, setLoading] = createSignal<boolean>(true);

  // fetchData zum Abrufen der Daten von der API
  async function fetchData() {
    setLoading(true); // Setze den Ladezustand auf true
    try {
      const response = await axios.get("http://localhost:8080/api/shopping/");
      if (response.status === 200) {
        // Erfolgreich geladen
        setItems(response.data);
      }
    } catch (err) {
      const error = err as AxiosError;  // Fehler als AxiosError typisieren

      if (error.response) {
        // Server hat geantwortet mit einem Fehlercode
        console.error(`Error: ${error.response.status} - ${error.response.statusText}`);
      } else if (error.request) {
        // Keine Antwort erhalten
        console.error("No response received from server");
      } else {
        // Fehler beim Anfragen
        console.error("Error in setting up the request");
      }
    } finally {
      setLoading(false); // Ladezustand auf false setzen, egal ob erfolgreich oder nicht
    }
  }

  // Funktion zum Aktualisieren der Menge eines Artikels
  const updateAmount = async (name: string, newAmount: number) => {
    try {
      await axios.put(`http://localhost:8080/api/shopping/${name}/update`, {
        amount: newAmount,
      });
      alert(`Updated ${name} successfully`);
      fetchData(); // Liste nach dem Update erneut abrufen
    } catch (error) {
      alert("Failed to update item");
      console.error("Error updating item:", error);
    }
  };

  // Funktion zum Löschen eines Artikels
  const deleteItem = async (name: string) => {
    try {
      await axios.delete(`http://localhost:8080/api/shopping/${name}/delete`);
      alert(`Deleted ${name} successfully`);
      fetchData(); // Liste nach dem Löschen erneut abrufen
    } catch (error) {
      alert("Failed to delete item");
      console.error("Error deleting item:", error);
    }
  };

  // Nutze onMount, um fetchData aufzurufen, wenn die Komponente gerendert wird
  onMount(() => {
    fetchData();
  });

  return (
    <div class={styles.container}>
      <h2 class={styles.header}>Shopping Items</h2>
      <button class={styles.button} onClick={() => fetchData()}>Refresh List</button>
      <ul>
        {loading() && <li>Loading...</li>}
        {!loading() && items().map((item) => (
          <li>
            {item.name} - {item.amount}
            <input
              type="number"
              min="1"
              value={item.amount}
              onInput={(e) => updateAmount(item.name, parseInt(e.currentTarget.value))}
            />
            <button onClick={() => deleteItem(item.name)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ShoppingList;
