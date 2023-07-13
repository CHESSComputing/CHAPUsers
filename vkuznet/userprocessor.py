from CHAP.pipeline import PipelineItem

class UserProcessor(PipelineItem):
    """Generic user processor.
    """

    def process(self, data):
        """Extract the contents of the input data, add a string to it,
        and return the amended value.

        :param data: input data
        :return: processed data
        """
        # If needed, extract data from a returned value of Reader.read
        #if isinstance(data, list):
        #    if all(isinstance(d, dict) for d in data):
        #        data = data[0]['data']
        #if data is None:
        #    return []

        # user code

        ### Welcome to CHAP notebook, user vkuznet

        # CHAP imports
        from CHAP.pipeline import PipelineItem
        # define pipeline object
        pipeline = PipelineItem()
        
        # I will add more code later
        
        # basic analysis
        from nexusformat.nexus import NXgroup
        nxobject = pipeline.unwrap_pipelinedata(data)
        
        # Find the NXdata in nxobject
        def get_nxdata(nxgroup):
            nxdata = nxgroup.plottable_data
            if nxdata is not None:
                return nxdata
            for k, v in nxgroup.items():
                if isinstance(v, NXgroup):
                    nxdata = get_nxdata(v)
                    if nxdata is not None:
                        return nxdata
        nxdata = get_nxdata(nxobject)
        
        # matplotlib imports
        import matplotlib.pyplot as plt
        # Plot the NXdata & return a matplotlib figure
        fig, ax = plt.subplots()
        self.logger.info("nxdata")
        print(nxdata.tree)
        nxdata.plot(figure=fig)
        

        # and we return data back to pipeline
        return data
