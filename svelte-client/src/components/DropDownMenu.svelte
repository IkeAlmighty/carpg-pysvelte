<script>

    export let options = [];
    export let setView = (view) => {
        console.log('Using the default (empty) setView() function. Pass your own set view function in to make the DropDownMenu interactive.')
    }

    let menuIsVisible = false;

    function callSetView(view) {
        setView(view);
        menuIsVisible = false;
    }

</script>

<div class="container">
    <button on:click={()=>{menuIsVisible = !menuIsVisible}}>
        {#if menuIsVisible}
            uneM
        {:else}
            Menu
        {/if}
    </button>

    {#if menuIsVisible}
        <div class = "dropdown">
            {#each options as option}
                <div class = "menu-option" on:click={()=>{callSetView(option.view)}}>{option.label}</div>
            {/each}
        </div>
    {/if}
</div>

<style>
    button {
        display: block;
    }

    div {
        width: 100%;
    }

    div button {
        float: left;
    }

    .dropdown {
        display: block;
        position: fixed;
        top: 5.2rem;
        left: 0;
        padding-left: 1.6rem;
        padding-top: 1rem;
        background-color: white;
        width: 100%;
        height: 100vh;
        background-color: lightgray;
    }

    .container {
        display: block;
        width: 100%;
    }

    .menu-option {
        padding: 0.4rem;
        padding-left: 0px;
        margin-left: 0;
        font-size:x-large;
    }

    .menu-option:hover {
        cursor: pointer;
    }

    .menu-option:active {
        opacity: 0.3;
        background-color: black;
        color: white;
    }
</style>