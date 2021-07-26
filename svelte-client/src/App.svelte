<script>
  import DropDownMenu from "./components/DropDownMenu.svelte";
  import SvelteMarkdown from "svelte-markdown";

  import { fetchRules } from "./utilities/endpoints";

  import Characters from "./views/Characters.svelte";
  import Incantations from "./views/Incantations.svelte";
  import Items from "./views/Items.svelte";
  import Spells from "./views/Spells.svelte";
  import { onMount } from "svelte";
  // import Planets from "./views/Planets.svelte";

  let View = undefined;
  let rulesmd = undefined;
  onMount(() => {
    fetchRules().then((res) => {
      rulesmd = res.data;
    });
  });
</script>

<main>
  <div class="menubar">
    <DropDownMenu
      options={[
        { view: Items, label: "Items" },
        { view: Incantations, label: "Incantations" },
        { view: Spells, label: "Spells" },
        { view: Characters, label: "Characters" },
      ]}
      setView={(view) => {
        View = view;
      }}
    />
  </div>

  {#if View}
    <svelte:component this={View} />
  {/if}

  {#if !View}
    <div id="default-view">Choose an option from 'Menu' to get started.</div>
  {/if}

  {rulesmd}
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
