<script>
  import OptionsBar from "./components/OptionsBar.svelte";
  import Items from "./views/Items.svelte"
  let View = undefined;
</script>

<main>
  <OptionsBar />
  {#if View}
    <View />
  {:else}
    <Items />
  {/if}
</main>

<style>
  main {
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  .d-block {
    display: block;
  }

  .text-small {
    font-size: smaller;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
