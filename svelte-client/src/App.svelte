<script>
  import OptionsBar from "./components/OptionsBar.svelte";
  import Characters from "./views/Characters.svelte";
  import Items from "./views/Items.svelte";
</script>

<main>
  <div class="view-container">
    <Items />
    <Characters />
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
  }

  .view-container {
    display: flex;
    flex-direction: row;
  }
</style>
