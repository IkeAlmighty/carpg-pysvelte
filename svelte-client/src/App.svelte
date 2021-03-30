<script>
  import Characters from "./views/Characters.svelte";
  import Incantations from "./views/Incantations.svelte";
  import Items from "./views/Items.svelte";
  import Spells from "./views/Spells.svelte";

  let View = Items;

</script>

<main>
  <div class="view-container">
    <View />
    <Characters />
    <Spells />
    <Incantations />
  </div>
</main>

<style>
  main {
    padding: 1em;
    max-width: 240px;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }

    .view-container {
      display: flex;
      flex-direction: column;
    }
  }

  .view-container {
    display: flex;
    flex-direction: row;
  }
</style>
