<script>
  import OptionsBar from "./components/OptionsBar.svelte";
  import { onMount } from "svelte";
  import axios from "axios";

	const API_URI = 'http://localhost:5000/api/hello'

  let items = undefined;

  onMount(async () => {
    axios.get(API_URI).then((res) => {
      items = res.data;
    });
  });

  let View = undefined;
</script>

<main>
  <OptionsBar />
  {#if View}
    <View />
  {:else}
    <span>select a tool! {items}</span>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
