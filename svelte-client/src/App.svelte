<script>
  import DropDownContainer from "./components/DropDownContainer.svelte";

  import Characters from "./views/Characters.svelte";
  import Incantations from "./views/Incantations.svelte";
  import Items from "./views/Items.svelte";
  import Spells from "./views/Spells.svelte";
  // import Planets from "./views/Planets.svelte";
</script>

<main>
  <div class="tool-container">
    <DropDownContainer child={Items} panelName="Item Generator" />
    <DropDownContainer child={Characters} panelName="Character Builder" />
    <DropDownContainer child={Spells} panelName="Spell Generator" />
    <DropDownContainer
      child={Incantations}
      panelName="Incantation Translator"
    />
  </div>
  <div class="notepad"><div editable /></div>
</main>

<style>
  main {
    padding: 1em;
    max-width: 240px;
  }

  .notepad {
    width: 100%;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }

    .tool-container {
      display: flex;
      flex-direction: column;
    }
  }

  .tool-container {
    display: flex;
    flex-direction: row;
  }
</style>
