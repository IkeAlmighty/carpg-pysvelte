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
      {view: Items, label: "Items"},
      {view: Incantations, label: "Incantations"},
      {view: Spells, label: "Spells"},
      {view: Characters, label: "Characters"},
      ]}
      setView={(view)=>{
        View = view;
      }}/>
  </div>
  
  {#if View} 
    <svelte:component this={View} />
  {/if}

  {#if !View}
    <div id='default-view'>Choose an option from 'Menu' to get started.</div>
  {/if}
</main>

<style>
  main {
    padding: 1em;
    max-width: 600px;
  }

  .menubar {
    display: flex;
    flex-direction: row;
  }

  #default-view {
    margin: 20vh auto;
    text-align: center;
  }
</style>
