<script>
  import { onMount } from 'svelte';
  import paper from 'paper';

  let planetdata = undefined;

  onMount(()=>{
    paper.install(window);
    paper.setup('map-canvas');
    
  })
</script>

<div class="container">
  {#if planetdata}
    <canvas id='map-canvas'></canvas>
  {/if}
</div>