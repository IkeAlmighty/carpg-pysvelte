<script>
  import DropDownMenu from "./components/DropDownMenu.svelte";

  import Characters from "./views/Characters.svelte";
  import Incantations from "./views/Incantations.svelte";
  import Items from "./views/Items.svelte";
  import Spells from "./views/Spells.svelte";
  // import Planets from "./views/Planets.svelte";

  let View = undefined;
</script>

<main>
  <div class="menubar">
    <DropDownMenu options = {[
      {view: Characters, label: "Characters"},
      {view: Incantations, label: "Incantations"},
      {view: Items, label: "Items"},
      {view: Spells, label: "Spells"},
      ]}
      setView={(view)=>{
        View = view;
      }}/>
  </div>
  
  {#if View} 
    <svelte:component this={View} />
  {/if}
</main>

<style>
  main {
    padding: 1em;
  }

  .menubar {
    display: flex;
    flex-direction: row;
  }
</style>
