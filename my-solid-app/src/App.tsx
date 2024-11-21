import type { Component } from "solid-js";
import ShoppingList from "./ShoppingList";
import AddItemForm from "./AddItemForm";
import styles from "./Style.module.css";

const App: Component = () => {
  return (
    <div class={styles.container}>
      <h1>My Shopping List App</h1>
      <AddItemForm />
      <ShoppingList />
    </div>
  );
};

export default App;
